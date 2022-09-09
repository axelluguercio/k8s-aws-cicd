FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
#ENV NGINX-CONF=${NGINX-CONF}
COPY nginx-test.conf /etc/nginx/conf.d

WORKDIR /usr/src/app