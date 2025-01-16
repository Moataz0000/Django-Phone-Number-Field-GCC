# phonevalidatorGCC/strategies/qatar.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class QatarPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('33', '55', '66', '77')):
            raise ValidationError('Qatari phone number must begin with 33, 55, 66, or 77.')
        if len(value) != 8:
            raise ValidationError('Qatari phone number must be 8 digits long.')