FROM node:latest

ENV TZ=Asia/Tokyo

WORKDIR /src
COPY ./frontend/package.json .
COPY ./frontend/package-lock.json .
RUN npm install
COPY ./frontend .
CMD ["npm", "run", "dev"]