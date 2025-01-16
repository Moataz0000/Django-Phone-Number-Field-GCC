# phonevalidatorGCC/factory.py
from ..strategies.egypt import EgyptPhoneValidationStrategy
from ..strategies.kuwait import KuwaitPhoneValidationStrategy
from ..strategies.oman import OmanPhoneValidationStrategy
from ..strategies.qatar import QatarPhoneValidationStrategy
from ..strategies.uae import UAEPhoneValidationStrategy
from ..strategies.bahrain import BahrainPhoneValidationStrategy
from ..strategies.saudi import SaudiPhoneValidationStrategy
from ..strategies.base import PhoneValidationStrategy

class PhoneValidationStrategyFactory:
    @staticmethod
    def get_strategy(country_code: str) -> PhoneValidationStrategy:
        if country_code == 'EG':
            return EgyptPhoneValidationStrategy()
        elif country_code == 'SA': 
            return SaudiPhoneValidationStrategy()
        elif country_code == 'KW':
            return KuwaitPhoneValidationStrategy()
        elif country_code == 'OM':
            return OmanPhoneValidationStrategy()
        elif country_code == 'QA':
            return QatarPhoneValidationStrategy()
        elif country_code == 'AE':
            return UAEPhoneValidationStrategy()
        elif country_code == 'BH':
            return BahrainPhoneValidationStrategy()
        else:
            raise ValueError(f'Unsupported country code: {country_code}')