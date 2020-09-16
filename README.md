# Python-Django-Deployment

## Running The Setup

         1. Install Docker on your system
         2. Install Docker-compose on your system


## Command to run the setup
  
         sudo docker-compose up --build( to build the project for first time or rebuilding it)
               
         
         
## Run Migration By:-

        
         sudo docker ps
         
  Output is the list of all conatiners running
         
  Get into the container:-
  
         sudo docker exec -it <conatiner-id> bash
         
  Then run the following command:-
  
         python manage.py migrate
  
         
               
