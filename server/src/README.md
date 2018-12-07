## Notes on how to change the resources that are driving the App

Server folder holds the backend implmentation of the Web App. The app implements scripts, main_script and Plinko_Model that were recieved from the client. Those scripts take csv files as an input and output 4 different files (Step-by-step Changes* and Final Plans for Scenerio Prostate*). These files are used in process_data script to read and select the information necessary based on the input from the user. In order to obtain these files, uncomment the main function in the main script and run it with python main_script.py. Once that is done comment the main function again and the app is ready to use. If you want different mapping that can be reassigned in the process data script.

## Limitation of the provided data
Copy QHP stores the insurance information that is used as an input in the main script file, nevertheless the QHP file contains hundreds of different insurance plans and client only wanted few options (Duke Data), thus the provided QHP file could not be fully utilized as we were randomly mapping Duke insurance provided by the users to the insurances in the file. In order for the app to be complete functional correct insurance information should be provided and that way all the specific plans could be mapped to one plan and its information would be an average. Or the user could be asked to provide specific plan rather then the specific insurance company and wider plan.
These are the considerations that need to be taken into account for future development.

## Server host
 Shows the server is up and running
    @ https://costcoachserver.herokuapp.com

## To run the server localy
1. initialize the dev environment
2. run the run.py