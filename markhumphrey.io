server {
    listen 80;
    server_name 192.168.99.100;

    location / {
        include uwsgi_params;
        uwsgi_pass web:8080;
    }
}
