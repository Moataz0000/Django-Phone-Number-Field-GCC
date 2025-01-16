# phonevalidatorGCC/observers.py
from abc import ABC, abstractmethod


class PhoneValidationObserver(ABC):
    """
    Base class for phone validation observer.
    """
    
    @abstractmethod
    def on_validation_success(self, value: str):
        pass
    
    def on_validation_failure(self, value: str, error: str):
        pass
    


class LoggingObserver(PhoneValidationObserver):
    """
    Logs validation results.
    """
    
    def on_validation_success(self, value: str):
        print(f'Validation succeeded for: {value}')

    def on_validation_failure(self, value: str, error: str):
        print(f'Validation failed for {value}: {error}')