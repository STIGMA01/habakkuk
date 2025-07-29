

## default.conf 예시

```conf
# nginx/conf.d/default.conf (예시)
server {
    listen 80;
    server_name localhost; # 또는 실제 도메인

    # 프론트엔드 (Vue.js) 정적 파일 서빙
    # frontend_dist 볼륨과 연결될 경로 (Docker Compose에서 설정)
    root /var/www/frontend;
    index index.html index.htm;

    # Vue Router의 HTML5 History Mode를 위한 설정
    # 존재하지 않는 경로 요청 시 index.html을 반환하여 Vue Router가 처리하게 함
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API 요청을 백엔드 (Django)로 리버스 프록시
    location /api/ {
        proxy_pass http://backend:8000; # backend 서비스의 8000번 포트로 연결
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Django 정적 파일 서빙 (static_volume과 연결될 경로)
    location /static/ {
        alias /var/www/static/; # backend 서비스의 static_volume에 해당
    }

    # Django 미디어 파일 서빙 (media_volume과 연결될 경로)
    location /media/ {
        alias /var/www/media/; # backend 서비스의 media_volume에 해당
    }

    # 에러 페이지 설정 (선택 사항)
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```

## 예시 2

```conf
# nginx/conf.d/default.conf
server {
    listen 80;
    server_name localhost;

    root /var/www/frontend;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ /index.html; # Vue Router History Mode
    }

    location /api/ {
        proxy_pass http://backend:8000;
        # ... (기타 프록시 설정) ...
    }

    location /static/ {
        alias /var/www/static/;
    }

    location /media/ {
        alias /var/www/media/;
    }
}

```


