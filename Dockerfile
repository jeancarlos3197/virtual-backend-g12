FROM node:18-alpine

WORKDIR /app

# COPY package.json /app/
# COPY package-lock.json /app/
COPY . /app/

RUN npm install

# COPY /src /app/src

CMD ["npm", "run", "start:dev"]