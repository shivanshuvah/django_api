# django_api

This is a django application, based on minimalistic design, which has 2 REST APIs:-
Api#1 - validate a slot with a finite set of values
Api#2 - validate a slot with a numeric value extracted and constraints on the value extracted

DOCKER IMAGE SIZE == 84.8 MB

To Run the project without docker, download the project, navigate to validationapi folder and run the below command : - 
`django-admin runserver --pythonpath=. --settings=settings`

The urls/endpoints of the application are:-
1. http://127.0.0.1:8000/finitevalues/
2. http://127.0.0.1:8000/numericvalues/

Sample Json Requests and corresponsing Json reponses are: - 
1. http://127.0.0.1:8000/finitevalues/

Request - 
{
  "invalid_trigger": "invalid_ids_stated",
  "key": "ids_stated",
  "name": "govt_id",
  "reuse": true,
  "support_multiple": true,
  "pick_first": false,
  "supported_values": [
    "pan",
    "aadhaar",
    "college",
    "corporate",
    "dl",
    "voter",
    "passport",
    "local"
  ],
  "type": [
    "id"
  ],
  "validation_parser": "finite_values_entity",
  "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
}

Response - 
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "ids_stated": ["COLLEGE"]
    }
}



2. http://127.0.0.1:8000/numericvalues/

Request - 
{
  "invalid_trigger": "invalid_age",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
}

Response - 
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "age_stated": 23
    }
}
