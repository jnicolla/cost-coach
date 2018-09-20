#!/bin/bash

# install client dependencies
cd client
npm install

# set up python environment and install dependencies
cd ../server
py -m venv env
source env/Scripts/activate