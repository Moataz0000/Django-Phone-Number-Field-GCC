from abc import ABC, abstractmethod
from django.core.exceptions import ValidationError


class PhoneValidationStrategy(ABC):
    """
    Base class for phone number validation strategies.
    """
    
    @abstractmethod
    def validate(self, value: str):
        """Validate the phone number"""
        pass