FROM node:14.20.0-alpine3.16 as build-stage

# set working directory
WORKDIR /usr/src/app

# add '/usr/src/app/node_modules/.bin' to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY ./package.json /usr/src/app/
COPY ./yarn.lock /usr/src/app/
RUN yarn
COPY . /usr/src/app
RUN yarn build

# stage 2 - build the final image and copy the react build files
FROM nginx:1.17.8-alpine

COPY --from=build-stage /usr/src/bundles/assets /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]