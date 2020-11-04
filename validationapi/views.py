from django.http import HttpResponse
from django.http import JsonResponse
import json

def finitevalues(request):
    if request.method=='POST':
        request_payload=json.loads(request.body)
        filled, partially_filled, trigger, parameters=validate_finite_values_entity(**request_payload)
        response_data = {
        'filled': filled,
        'partially_filled': partially_filled,
        'trigger' : trigger,
        'parameters':parameters
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Invalid Request!")

def validate_finite_values_entity(values=[],supported_values=[],invalid_trigger=None,key=None,support_multiple=True,pick_first=False,**kwargs):
    validations = []#bool list
    valid_values = []
    for utterance in values:
        if utterance['entity_type'] in kwargs['type'] and utterance['value'] in supported_values:
            validations.append(True)
            valid_values.append(utterance['value'])
        else:
            validations.append(False)
    if validations: #condition :there are values
        if all(validations):
            filled=True
            partially_filled= False #all values true
            trigger=""#all values supported
            if pick_first: 
                param_values=valid_values[0] #return only first value if pick_first is True
            elif not pick_first and support_multiple:
                param_values=valid_values
            else:
                param_values=valid_values #raise error here

            parameters={key:param_values}
        else:
            filled = False
            partially_filled=True #subset is valid
            trigger=invalid_trigger # invalid values stated
            parameters={}
    else: #no values
       filled=False 
       partially_filled=False
       trigger=invalid_trigger
       parameters={}
    return (filled, partially_filled, trigger, parameters)

def numericvalues(request):
    if request.method=='POST':
        request_payload=json.loads(request.body)
        filled, partially_filled, trigger, parameters=validate_numeric_entity(**request_payload)
        response_data = {
        'filled': filled,
        'partially_filled': partially_filled,
        'trigger' : trigger,
        'parameters':parameters
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Invalid Request!")

def validate_numeric_entity(values=[],invalid_trigger=None, key=None, support_multiple=True, pick_first=False, constraint=None,var_name=None, **kwargs):
    validations=[]
    valid_values=[]
    if constraint is None or not constraint.strip():
        for utterance in values:#checks needed for partially_filled
           valid_values.append(utterance['value'])
           validations.append(True)
    else:
        for utterance in values:
            if utterance['entity_type'] in kwargs['type'] and eval(constraint,{},{var_name:utterance['value']}):
                validations.append(True)
                valid_values.append(utterance['value'])
            else:
                validations.append(False)
    if validations: #condition :there are values
        if all(validations):
            filled=True
            partially_filled= False #all values true
            trigger=""#all values supported
            if pick_first: 
                param_values=valid_values[0] #return only first value if pick_first is True
            elif not pick_first and support_multiple:
                param_values=valid_values
            parameters={key:param_values}
        else:
            filled = False
            partially_filled=True #subset is valid
            trigger=invalid_trigger # invalid values stated
            if len(valid_values)>0:
                if pick_first: 
                    param_values=valid_values[0] #return only first value if pick_first is True
                elif not pick_first and support_multiple:
                    param_values=valid_values
                parameters={key:param_values}
            else:
                parameters={}
    else: #no values
       filled=False 
       partially_filled=False
       trigger=invalid_trigger
       parameters={}
    return (filled, partially_filled, trigger, parameters)   



