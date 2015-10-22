server {
    listen 80;
    server_name 192.168.99.100;
    root /usr/share/nginx/html/;
    location / { try_files $uri @app; }

    location @app {
        include uwsgi_params;
        uwsgi_pass web:8080;
    }

}
