#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django.conf


def main():
    """Run administrative tasks."""
    # 从环境变量获取 PROJECT_ENV 读取 config.django 目录下对应的配置文件，默认读取 dev 环境
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.django.{os.environ.get("PROJECT_ENV", default="dev")}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
