FROM node:25-alpine3.21

#workdir->directory corrente del container
WORKDIR /app 
COPY . .
RUN npm install
EXPOSE 5173
# CMD non ci serve perchè tireremo su tutto con docker compose

#il docker file serve per specificare un solo SERVIZIO
#il docker-compose invece compone i vari dockerfile/servizi

