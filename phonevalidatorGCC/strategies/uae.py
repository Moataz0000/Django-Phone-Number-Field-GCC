# phonevalidatorGCC/strategies/uae.py
from django.core.exceptions import ValidationError
from .base import PhoneValidationStrategy

class UAEPhoneValidationStrategy(PhoneValidationStrategy):
    def validate(self, value: str):
        if not value.startswith(('050', '051', '052', '054', '055', '056', '058')):
            raise ValidationError('UAE phone number must begin with 050, 051, 052, 054, 055, 056, or 058.')
        if len(value) != 9:
            raise ValidationError('UAE phone number must be 9 digits long.')