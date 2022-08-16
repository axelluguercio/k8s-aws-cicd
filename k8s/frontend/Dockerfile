FROM node:latest as build-stage

# set working directory
RUN mkdir /usr/app

COPY . /usr/app

WORKDIR /usr/app

# install and cache app dependencies
RUN yarn

# add '/usr/src/app/node_modules/.bin' to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

RUN npm run build

# stage 2

# copy the content builed in stage 1
FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# remove default nginx static assets
RUN rm -rf ./*

# copy statis assests from builder stage
COPY --from=build-stage /usr/assets/bundles .

# containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]