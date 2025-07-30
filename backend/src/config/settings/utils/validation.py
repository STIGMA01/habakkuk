"""
**Settings Validation**

Mitigates several issues that could arise during Django operation.

"""
import os
import sys
from abc import ABC, abstractmethod
from typing import Callable, Optional, Iterable, Type, Tuple
from django.core.exceptions import ValidationError



def exec_validate_settings(module_name, additional_patterns: list=None):
    """
    **module_name**: __name__ of module(this)  
    **additional_patterns**: list[SettingsValidateGeneralPattern]  
    """
    default_patterns = [
        SettingsValidateGeneralPattern(key="SECRET_KEY", truthiness_check=True, type_check=str),
    ]

    validator = SettingsValidator(sys.modules[module_name], 
                                  default_patterns + additional_patterns if additional_patterns else [])
    validator.validate()



class Validatable(ABC):
    """Abstract base class for all settings validation patterns."""
    def __init__(self):
        self._settings = None

    def set_settings(self, value):
        """Sets the Django settings object for the validator."""
        self._settings = value
        return self

    @abstractmethod
    def validate(self) -> None:
        """
        Performs the specific validation logic.
        Should raise ValidationError if validation fails.
        """
        pass


class SettingsValidateGeneralPattern(Validatable):
    """
    A general-purpose validation pattern for a single Django setting key.

    This pattern allows checking for existence, truthiness, type, and
    provides an optional custom validation function.
    """
    def __init__(self,
                 key: str,
                 truthiness_check: bool = False, 
                 type_check: Optional[Type | Tuple[Type]] = None,
                 additional_validate_func: Optional[Callable[[any], None]] = None):
        super().__init__()
        self._key = key
        self._truthiness_check = truthiness_check
        self._type_check = type_check
        self._additional_validate_func = additional_validate_func

    def validate(self) -> None:
        """
        Validates the specific setting defined during initialization.
        Raises ValidationError on failure.
        """
        if not hasattr(self._settings, self._key):
            raise ValidationError(f"Settings variable '{self._key}' has not been set. Please check your Django settings.")

        setting_value = getattr(self._settings, self._key)

        if self._truthiness_check and not setting_value:
            raise ValidationError(
                f"Settings variable '{self._key}' is truthy-checked but its value is "
                f"{setting_value!r} (Type: {type(setting_value).__name__}). "
                f"It must not be null or empty."
            )

        if self._type_check is not None and not isinstance(setting_value, self._type_check):
            expected_types_str = (
                self._type_check.__name__ if isinstance(self._type_check, Type)
                else ', '.join(t.__name__ for t in self._type_check)
            )
            raise ValidationError(
                f"The type of settings variable '{self._key}' must be {expected_types_str}. "
                f"Current type: {type(setting_value).__name__} (Value: {setting_value!r})."
            )

        if self._additional_validate_func:
            try:
                self._additional_validate_func(setting_value)
            except ValidationError as e:
                raise e
            except Exception as e:
                raise ValidationError(
                    f"Custom validation for '{self._key}' failed due to an unexpected error: {e}"
                ) from e


class SettingsValidator:
    """
    Main validator class to run all defined validation patterns against Django settings.
    """
    def __init__(self, django_settings, validate_patterns: Iterable[Validatable]):
        self._settings = django_settings
        self._patterns: list[Validatable] = []
        for pattern in validate_patterns:
            pattern.set_settings(django_settings) 
            self._patterns.append(pattern)

    def validate(self) -> None:
        """
        Runs all registered validation patterns against the Django settings.

        This ensures that critical settings are correctly configured before application startup,
        thereby preventing common security problems, human errors, and typing mistakes.
        """
        errors = []
        for pattern in self._patterns:
            try:
                pattern.validate()
            except ValidationError as e:
                errors.append(e)

        if errors:
            print("\n" + "="*50)
            print("ERROR: Django settings validation failed!")
            for error in errors:
                print(f"- {error.message}")
            print("="*50 + "\n")
            sys.exit(1)
        # else:
        #     print("Django settings validation successful!")
