## Typeform_data_API
The python file Typeform_API.py requests data forms from Typeform website which corresponds
to customer responses to a typeform questionare (e.g. marketing research) using a specific API key of a specific registered account and then firstly save the raw data into a json
file consequently parsing the json objects as pyton objects and then produce a single table containing
all the responses objects in a CSV file.
Specifically, our table contains responses from both the answers and the metadata parts of the data 
form.


The final output.csv file contains a table
with each row representing each type of responses object (e.g. "list_46100308_choice","textarea_46098446","network_id" etc)
and with each column representing each user response.
