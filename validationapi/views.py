from django.http import HttpResponse
from django.http import JsonResponse
import json
from implementation import validate_finite_values_entity, validate_numeric_entity

def finitevalues(request):
    try:
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
            return JsonResponse({'BadRequest':'Method other than POST'}, status=400, safe=False)
    except Exception as e:
        return JsonResponse(str(e), status=500, safe=False) #server encountered error



def numericvalues(request):
    try:
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
            return JsonResponse({'BadRequest':'Method other than POST'}, status=400, safe=False)
    except Exception as e:
        return JsonResponse(str(e), status=500, safe=False) #server encountered error





