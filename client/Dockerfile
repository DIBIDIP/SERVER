# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /frontend

# `/app/node_modules/.bin`을 $PATH 에 추가
ENV PATH /frontend/node_modules/.bin:$PATH

# app dependencies, install 및 caching
COPY package.json /frontend/package.json
RUN npm install
RUN npm install react-scripts@3.0.1 -g

COPY . /frontend

# 정적파일 생성
RUN npm run build