# Use a lightweight Node.js image as the base
FROM node:20.18

# Set the working directory in the container
WORKDIR /app

# Copy package.json to install dependencies
COPY package.json ./
COPY package-lock.json ./

# Copy code
COPY ./src              ./src
COPY ./static           ./static
COPY ./vite.config.js   ./vite.config.js
COPY ./svelte.config.js ./svelte.config.js
COPY ./.svelte-kit      ./.svelte-kit

# Install dependencies
RUN npm install
EXPOSE 80
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "80"]