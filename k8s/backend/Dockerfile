# Build stage

FROM python:3.7-alpine

# set work directorry
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev \
    postgresql-dev postgresql-libs jpeg-dev zlib-dev \
    freetype-dev lcms2-dev \ 
    openjpeg-dev tiff-dev tk-dev \
    tcl-dev harfbuzz-dev fribidi-dev \
    graphviz g++ make swig linux-headers graphviz-dev \
    postgresql-libs libstdc++

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy app 
COPY ./django_app . 

# una vez instalado los requerimientos elimina las dependecias en cache y instala la libreria para postgresql
RUN apk del build-deps && \
    apk add netcat-openbsd postgresql-libs && \
    rm requirements.txt && \
    chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]