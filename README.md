# CostCoach

A web application that calculates out-of-pocket treatment costs for cancer patients.<br/>

CS 408 project documents (e.g. executive summary) can be found in the "project_docs" directory.<br/>

## Notes

To set up the repository locally, you must have Node.js and Python installed. This app was initially developed in Node.js v8.11.4 and Python 3.6, so make sure you are using the latest versions, especially with Python.<br/>
**Mac users** must install XCode and Homebrew before trying to install Node.js or Python. Instructions can be found [here](http://blog.teamtreehouse.com/install-node-js-npm-mac)<br/>
<br/>
Open two terminals; cd into the client directory in one of the terminals and the server directory in the other.<br/>
<br/>
In the **client** terminal, execute "npm install". Then type "npm install nodemon". Nodemon is a tool that allows you to see changes you've made to the frontend without having to restart the app. Once nodemon is installed, type "nodemon" into the terminal and execute.<br/>
<br/>
In the **server** terminal, initialize a Python virtual environment. This is done to allow packages specific to the project to be installed within the project scope. Activate the environment once it is initialized and run "pip install -r requirements.txt". Then start the Flask app by typing "py app.py".<br/>
<br/>
Open up a browser and navigate to "[localhost:8080](localhost:8080)". You are ready to begin developing.<br/>
**Note** You must activate the Python virtual environment each time you want to run the server (i.e. use "py app.py"). To do this, execute the command "source env/Scripts/activate". You must also run "nodemon" to be able to see the website.

Update Check - 9/30/18

