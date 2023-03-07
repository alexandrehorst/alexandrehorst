Customer/ patient management system:
- The motivation to write this code is because my wife is a dentist and I wanted to help her to automatize some how her office.  

- This program is based on list manipulation (cad -> the main list) that is composed of several sublists, which contain the information of each patient.

- The list can be loaded from an excel sheet (now) or a database (SQL database in the future roadmap).

- The patient data sublists are basically organized by: name, telephone, Address, patienet id (called CPF in Brazil), profession, e-mail, next appointment day, next appointment time and email sending flag.

- SW capabilities: patient registration, scheduling/rescheduling/unscheduling appointments (syncronized with a google calendar account), schedule view, patient data view, automatic email sending N days for patient requesting consultation confirmation and integration with google calendar (we need to make some configurations in your google account a token
creation)

- In the end, an excel file is generated with all data saved. Each time you run the program it is asked with you want to import the previous saved data or with you want to start a new session. In the future, I intend to have an integration with a SQL Database (It is on my Roadmap).  

- For automatic e-mail sending you will need to create a gmail APP password and insert a valid gmail account on line 134.

- To include, read, modify or exclude appointments using Google Calendar API it is necessary to follow the actions described in https://developers.google.com/calendar/api/quickstart/python. 

- Be careful for the right use of the json files 

- In your google account configuration you will need to create a project and enable the API use

- It's necessary to install the google-auth module (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib)

Program Roadmap:
- Create an executable version
- Deploy it in Google Clouds
- Integration with a SQL Database
- Create an user interface  
