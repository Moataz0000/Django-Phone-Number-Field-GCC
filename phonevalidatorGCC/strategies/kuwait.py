# phonevalidatorGCC/strategies/kuwait.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class KuwaitPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('5', '6', '9')):
            raise ValidationError('Kuwaiti phone number must begin with 5, 6, or 9.')
        if len(value) != 8:
            raise ValidationError('Kuwaiti phone number must be 8 digits long.')