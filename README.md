# PhoneValidatorX 📞

**A flexible and extensible phone number validation package for GCC countries and Egypt.**

[![PyPI Version](https://img.shields.io/pypi/v/phonevalidatorx?color=blue&label=PyPI%20Package)](https://pypi.org/project/phonevalidatorx/)
[![License](https://img.shields.io/pypi/l/phonevalidatorx?color=green)](https://pypi.org/project/phonevalidatorx/)
[![Python Version](https://img.shields.io/pypi/pyversions/phonevalidatorx?color=orange)](https://pypi.org/project/phonevalidatorx/)

---

## Overview

**PhoneValidatorX** is a Python package designed to validate phone numbers for **GCC countries** (Saudi Arabia, UAE, Qatar, Kuwait, Oman, Bahrain) and **Egypt**. It provides a **custom Django field** that can be easily integrated into your Django models, along with flexible validation options.

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