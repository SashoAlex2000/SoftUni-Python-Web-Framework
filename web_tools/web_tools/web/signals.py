from django.db.models import signals
from django.dispatch import receiver

from web_tools.web.models import Employee


# signals are used for separation of concerns, we cannot override the save() method always
# for example sending a mail on register, shouldn't be in save(), since it has no relation to DB

@receiver(signals.post_save, sender=Employee)
def handle_employee_created(*args, **kwargs):
    print(args)
    print(kwargs)
