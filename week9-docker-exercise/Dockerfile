#Base image ubuntu 18.04
FROM ubuntu:18.04

MAINTAINER Chenxu Wang

#update Ubuntu
RUN apt-get update

#Install Mongodb
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list
RUN apt-get update
RUN apt-get install -y mongodb-10gen
RUN mkdir -p /data/db

#Mount directory
VOLUME ["/data/db"]
#Expose default port
EXPOSE 27017

#Default command of mongodb
CMD ["mongod"]

#Command to create user
#use dbname
#db.createUser({user:"admin", pwd:"adminsecret", roles:[{role:"readWrite", db: "dbname"}]});


#Authentication enabled comman,
#docker run --name mongodb -v mongodata:/data/db -d -p 27017:27017 mongo --auth
#How to authenticate
#mongodb://admin:adminpassword@localhost:27017/dbname