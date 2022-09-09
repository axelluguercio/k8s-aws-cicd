FROM node:12.18.3-alpine3.9 as build-stage

# set working directory
WORKDIR /usr/src/app

COPY ./package.json .
# install dependencies and avoid `node-gyp rebuild` errors
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install \
    && apk del .gyp

# copy our react project
COPY ./ .

# add '/usr/src/app/node_modules/.bin' to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# perform npm build
ARG API_SERVER
ENV REACT_APP_API_SERVER=${API_SERVER}
RUN REACT_APP_API_SERVER=${API_SERVER} \ 
  npm run build

# stage 2

# copy the content builed in stage 1
# pull official base image
FROM node:12.18.3-alpine3.9 

# set work directory
WORKDIR /usr/src/app

# install serve - deployment static server suggested by official create-react-app
RUN npm install -g serve

# copy our build files from our builder stage
COPY --from=build-stage /usr/src/app/build ./build