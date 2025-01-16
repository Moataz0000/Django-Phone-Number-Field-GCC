# phonevalidatorGCC/strategies/oman.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class OmanPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('7', '9')):
            raise ValidationError('Omani phone number must begin with 7 or 9.')
        if len(value) != 8:
            raise ValidationError('Omani phone number must be 8 digits long.')