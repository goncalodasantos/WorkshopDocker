FROM node
WORKDIR /npmtest
RUN npm install yarn
RUN yarn add react
RUN yarn create react-app testapp
WORKDIR /npmtest/testapp
EXPOSE 3000