from os import getenv

def parse_env(key, default=None, force=False):
    e = getenv(key, default)
    if force and not e:
        raise EnvironmentError(f"Cannot parse environemtn variable! '{key}'")
    return e
