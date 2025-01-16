# phonevalidatorGCC/validator.py
from django.core.exceptions import ValidationError
from ..strategies.base import PhoneValidationStrategy
from .observers import PhoneValidationObserver




class PhoneValidator:
    """
    Context class for phone number validation.
    """
    
    
    def __init__(self, strategy: PhoneValidationStrategy):
        self.strategy = strategy
        self.observers = []
        
        
    def add_observer(self, observer: PhoneValidationObserver):
        self.observers.append(observer)
    
    def validate(self, value: str):
        try:
            self.strategy.validate(value)
            for observer in self.observers:
                observer.on_validation_success(value)
        except ValidationError as e:
            for observer in self.observers:
                observer.on_validation_failure(value, str(e))
            raise
        
