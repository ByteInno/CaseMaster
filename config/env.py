#!/usr/bin/env python
# @Project: CaseMaster
# @Author: https://github.com/HackSoftware/Django-Styleguide-Example/blob/master/config/env.py
# @File name: env
# @Create time: 2023/4/10 23:09

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()

BASE_DIR = environ.Path(__file__) - 2


def env_to_enum(enum_cls, value):
    for x in enum_cls:
        if x.value == value:
            return x
    raise ImproperlyConfigured(f"Env value {repr(value)} could not be found in {repr(enum_cls)}")
