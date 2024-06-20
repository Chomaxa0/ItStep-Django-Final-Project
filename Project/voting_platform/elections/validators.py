from django.core.exceptions import ValidationError
import re

def validate_alpha(value):
    if not re.match(r'^[a-zA-Zა-ჰ]+$', value):  
        raise ValidationError('Only English and Georgian alphabetic characters are allowed.')
