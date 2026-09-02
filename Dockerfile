# Idi mana base server (oka chinna web server)
FROM nginx:alpine

# Mana code antha aa server loki copy chesthundi
COPY . /usr/share/nginx/html
