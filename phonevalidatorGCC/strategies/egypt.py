# phonevalidatorGCC/strategies/egypt.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class EgyptPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('010', '011', '012', '015')):
            raise ValidationError('Egyptian phone number must begin with 010, 011, 012, or 015.')
        if len(value) != 11:
            raise ValidationError('Egyptian phone number must be 11 digits long.')