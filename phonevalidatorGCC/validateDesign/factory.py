# phonevalidatorGCC/factory.py
from strategies.base import PhoneValidationStrategy
from strategies.egypt import EgyptPhoneValidationStrategy
from strategies.saudi import SaudiPhoneValidationStrategy


class PhoneValidationStrategyFactory:
    """
    Factory class to create phone validation strategies.
    """
    
    @staticmethod
    def get_strategy(country_code: str) -> PhoneValidationStrategy:
        if country_code == 'EG':
            return EgyptPhoneValidationStrategy()
        elif country_code == 'SA': 
            return SaudiPhoneValidationStrategy()

        else:
            raise ValueError(f'Unsupported country code: {country_code}!')