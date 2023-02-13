from django.db.models import Manager


class DepartmentManager(Manager):
    def get_or_create_department_by_name(self, dname):
        # ensure we have the department
        try:
            return self.model.objects.filter(
                name=dname
            ).get()
        except self.model.DoesNotExist:
            return self.model.objects.create(
                name=dname,
            )


