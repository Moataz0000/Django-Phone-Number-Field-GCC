# phonevalidatorGCC/decorators.py
from django.core.exceptions import ValidationError
from strategies.base import PhoneValidationStrategy



class PhoneValidationDecorator(PhoneValidationStrategy):
    
    """
    Decorator to add additional validation rules.
    """
    
    def __init__(self, strategy: PhoneValidationStrategy):
        self.strategy = strategy
        
    
    def validate(self, value: str):
        if not value.isdigit():
            raise ValidationError('Phone number must contain only digits!')
        self.strategy.validate(value)