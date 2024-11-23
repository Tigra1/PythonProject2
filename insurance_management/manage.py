import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insurance_management.settings")

    port = os.environ.get("PORT", "8000")  # Используем порт из переменной окружения или значение по умолчанию

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    sys.argv = ["manage.py", "runserver", f"0.0.0.0:{port}"]
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
