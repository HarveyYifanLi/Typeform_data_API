## Typeform_data_API
The python file Typeform_API.py requests data froms from Typeform website using the 
specific API key of a specific user account and then firstly save the raw data into a json
file consequently parsing the json objects as pyton objects and produce a single table containing
all the responses objects in a CSV file.
Specifically, our table contains responses from both the answers and the metadata parts of the data 
form.


The final output.csv file contains a table having 12 columns and 16 rows,
with each column representing each type of responses object (e.g. "list_46100308_choice","textarea_46098446","network_id" etc)
and with each row representing each user response.
