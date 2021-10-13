from node:14

WORKDIR /code

COPY package.json .
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install tmux -y \
    && npm install 


# Instalación de Nodemon en forma Global
# Al realizarse cambios reiniciar el servidor
# RUN npm install nodemon -g --quiet


COPY . .

EXPOSE 8080

# Inicia la aplicación al iniciar al contenedor
# CMD nodemon -L --watch . app.js