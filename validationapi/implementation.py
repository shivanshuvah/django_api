def validate_finite_values_entity(values=[],supported_values=[],invalid_trigger=None,key=None,support_multiple=True,pick_first=False,**kwargs):
    """
    Validate an entity on the basis of its value extracted.
    The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param supported_values: List of supported values for the slot
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :return: a tuple of (filled, partially_filled, trigger, params)
    """    
    
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

def validate_numeric_entity(values=[],invalid_trigger=None, key=None, support_multiple=True, pick_first=False, constraint=None,var_name=None, **kwargs):
    """
    Validate an entity on the basis of its value extracted.
    The method will check if that value satisfies the numeric constraints put on it.
    If there are no numeric constraints, it will simply assume the value is valid.

    If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
    In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
    will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

    If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
    partially filled.

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :param constraint: Conditional expression for constraints on the numeric values extracted
    :param var_name: Name of the var used to express the numeric constraint
    :return: a tuple of (filled, partially_filled, trigger, params)
    """    
    
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