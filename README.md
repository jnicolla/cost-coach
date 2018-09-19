# CostCoach

A web application that calculates out-of-pocket treatment costs for cancer patients.<br/>

CS 408 project documents (e.g. executive summary) can be found in the "project_docs" directory.<br/>

## Notes

To set up the repository locally, you must have Node.js and Python installed. This app was initially developed in Node.js v8.11.4 and Python 3.6, so make sure you are using the latest versions, especially with Python.<br/>
**Mac users** must install XCode and Homebrew before trying to install Node.js or Python. Instructions can be found [here](http://blog.teamtreehouse.com/install-node-js-npm-mac)<br/>
<br/>
Run the script *setup.sh* by typing "bash setup.sh" in the terminal. Open two terminals; cd into the client directory in one of the terminals and the server directory in the other. Run the commands "nodemon" in the client terminal and "py app.py" in the server terminal, then open up a browser and navigate to "[localhost:8080](localhost:8080)". You are ready to begin developing.<br/>
<br/>
**Note** You must activate the Python virtual environment each time you want to run the server (i.e. use "py app.py"). To do this, execute the command "source env/Scripts/activate"