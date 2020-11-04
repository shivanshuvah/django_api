from django.http import JsonResponse
from django.views import View
import json
from implementation import validate_finite_values_entity, validate_numeric_entity

class FiniteValues(View):
    def post(self, request, *args, **kwargs):
        try:
            request_payload=json.loads(request.body)
            filled, partially_filled, trigger, parameters=validate_finite_values_entity(**request_payload)
            response_data = {
            'filled': filled,
            'partially_filled': partially_filled,
            'trigger' : trigger,
            'parameters':parameters
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False) #server encountered error


class NumericValues(View):
    def post(self, request, *args, **kwargs):
        try:
            request_payload=json.loads(request.body)
            filled, partially_filled, trigger, parameters=validate_numeric_entity(**request_payload)
            response_data = {
            'filled': filled,
            'partially_filled': partially_filled,
            'trigger' : trigger,
            'parameters':parameters
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False) #server encountered error





