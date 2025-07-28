FROM node:18-alpine

WORKDIR /app

COPY ./package.json ./package-lock.json* ./ 
RUN npm install

COPY . /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
