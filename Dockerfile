FROM debian:jessie-slim
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
WORKDIR /app
COPY . /app
