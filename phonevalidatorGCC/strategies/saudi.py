# phonevalidatorGCC/strategies/saudi.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class SaudiPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('050', '051', '052', '053', '054', '055', '056', '057', '058', '059')):
            raise ValidationError('Saudi phone number must begin with 050, 051, 052, etc.')
        if len(value) != 9:
            raise ValidationError('Saudi phone number must be 9 digits long.')