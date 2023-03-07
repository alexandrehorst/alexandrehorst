Office patient registration program:
- This program is based on list manipulation (called cad) that is composed of several sublists, which contain the information of each patient.

- The list can be loaded from an excel sheet (now) or a database (SQL database in the future roadmap).

- The patient data sublists are basically organized by: name, telephone, Address, CPF, profession, e-mail, next appointment day, next appointment time and email sending flag

- SW capabilities: patient registration, scheduling/rescheduling/unscheduling appointments, schedule view, patient data view, automatic email sending N days for patient requesting consultation confirmation and integration with google calendar (we need to make some configurations in your google account a token
creation)

- For automatic e-mail sending you will need to create a gmail APP password and insert it on line 134.

- For include, read, modify or exclude appointments using Google Calendar API follow the actions describede  in https://developers.google.com/calendar/api/quickstart/python. 

- Be careful for the right use of the json files 

- In your google account configuration you will need to create a project and enable the API use

- It's necessary to install the google-auth module (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib)
