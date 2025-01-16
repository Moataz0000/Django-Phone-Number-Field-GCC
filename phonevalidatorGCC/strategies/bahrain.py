# phonevalidatorGCC/strategies/bahrain.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class BahrainPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('3', '6', '9')):
            raise ValidationError('Bahraini phone number must begin with 3, 6, or 9.')
        if len(value) != 8:
            raise ValidationError('Bahraini phone number must be 8 digits long.')