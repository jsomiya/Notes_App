Note_Taking_App

Clone and run:

pip install -r requirements.txt    //for installing relevant packages

python manage.py makemigrations   //for creating the model

python manage.py migrate         //for applying the migration

python mange.py runserver       //to run the server



E.g. of a Note: 
title : Assignment
content : Note_Taking_App using Django and DRF
slug : assignment



URL :
1. New note -> http://localhost:8000/create/ 
2. Delete a note -> http://localhost:8000/delete_note/<slug>
3. Update a note -> http://localhost:8000/update_note/<slug>
4. List of Titles -> http://localhost:8000/title_list/
5. Detail of a particular note -> http://localhost:8000/details/<slug>







  



