from django.db import models
from django.core.exceptions import ValidationError
from .validateDesign.factory import PhoneValidationStrategyFactory
from .validateDesign.decorators import PhoneValidationDecorator
from .validateDesign.validator import PhoneValidator




class PhoneNumberField(models.CharField):
    """
    Custom Django field for phone number validation.
    """
    
    
    def __init__(self, allow_all_country=False, country_code=None, *args, **kwargs):
        kwargs.setdefault('max_length', 15)
        self.allow_all_country = allow_all_country
        self.country_code = country_code
        super().__init__(*args, **kwargs)
        
        
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        
        if value:
            if self.allow_all_country:
                # Validate for all GCC countries
                for code in ['EG', 'SA', 'AE', 'QA', 'KW', 'OM', 'BH']:
                    try:
                        strategy = PhoneValidationStrategyFactory.get_strategy(code)
                        decorated_strategy = PhoneValidationDecorator(strategy=strategy)
                        validator = PhoneValidator(decorated_strategy)
                        validator.validate(value=value)
                        return  # Validation succeeded for at least one country
                    
                    except ValidationError:
                        continue
                raise ValidationError('Phone number is not valid for any GCC country.')
            else:
                # Validate for the specified country
                if not self.country_code:
                    raise ValidationError('Country code must be specified when allow_all_country is False.')
                strategy = PhoneValidationStrategyFactory.get_strategy(self.country_code)
                decorated_strategy = PhoneValidationDecorator(strategy=strategy)
                validator = PhoneValidator(decorated_strategy)
                validator.validate(value=value)
