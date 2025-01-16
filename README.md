# Django_Phone_Number_Field_GCC 📞

**A flexible and extensible phone number validation package for GCC countries and Egypt.**

[![PyPI](https://img.shields.io/badge/PyPI-Logo-blue?logo=python&logoColor=white)](https://pypi.org/project/Django-GCC-PhoneNumbers/)

---

## Overview

**Django_Phone_Number_Field_GCC** is a Python package designed to validate phone numbers for **GCC countries** (Saudi Arabia, UAE, Qatar, Kuwait, Oman, Bahrain) and **Egypt**. It provides a **custom Django field** that can be easily integrated into your Django models, along with flexible validation options.

### Key Features:
- **Country-Specific Validation**: Validate phone numbers based on the country code (e.g., `EG` for Egypt, `SA` for Saudi Arabia).
- **Flexible Field Options**: Supports Django field arguments like `max_length`, `blank`, and `null`.
- **Allow All GCC Countries**: Optionally validate phone numbers for all GCC countries at once.
- **Extensible**: Easily add new countries or validation rules.

---

## Installation

Install the package via `pip`:

```bash
pip install phonevalidatorx
```

```bash
from django.db import models
from phonevalidatorGCC.fields import PhoneNumberField

class UserProfile(models.Model):
    # Example: Accept phone numbers from all GCC countries
    gcc_phone = PhoneNumberField(
        allow_all_country=True,
        max_length=15,
        blank=True,
        null=True,
        help_text="Enter a phone number from any GCC country."
    )

    # Example: Accept only Egyptian phone numbers
    egypt_phone = PhoneNumberField(
        country_code='EG', # Changeable for any of these ['EG', 'SA', 'AE', 'QA', 'KW', 'OM', 'BH']
        max_length=11,
        blank=False,
        null=False,
        help_text="Enter a valid Egyptian phone number."
    )

    def __str__(self):
        return f'GCC Phone: {self.gcc_phone}, Egypt Phone: {self.egypt_phone}'
```