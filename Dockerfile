FROM python:2.7

# TODO: this is not ideal and pulls in too much extra (for example python..again..)
# also does the image really still need npm and bower after the frontend dependencies are pulled down
# install npm to pull in bower for frontend dependencies
RUN apt-get update
RUN apt-get -y install nodejs
# handle debian naming the node binary nodejs
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN apt-get -y install npm

WORKDIR /my_app

# install python library requirements
RUN virtualenv /env
ADD requirements.txt /my_app/requirements.txt
RUN /env/bin/pip install -r /my_app/requirements.txt

# install front end libraries
ADD package.json /my_app/package.json
RUN npm install
ADD bower.json /my_app/bower.json
ADD .bowerrc /my_app/.bowerrc
RUN /my_app/node_modules/bower/bin/bower install --allow-root --config.interactive=false

ADD . /my_app

EXPOSE 8080
CMD ["/env/bin/python", "main.py"]
