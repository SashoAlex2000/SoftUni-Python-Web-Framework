from rest_framework import serializers

from rest_api_lecture.web_api.models import Employee, Department


# better to be put as manager on Department
# def get_or_create_department_by_name(dname):
#     # ensure we have the department
#     try:
#         return Department.objects.filter(
#             name=dname
#         ).get()
#     except Department.DoesNotExist:
#         return Department.objects.create(
#             name=dname,
#         )


# defines a short serializer, without the department, to be put into the department
class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'salary')


class DepartmentSerializer(serializers.ModelSerializer):
    # has to be named employee_set in order to work ;
    employee_set = ShortEmployeeSerializer(many=True)

    class Meta:
        model = Department
        fields = '__all__'


class ShortDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


# What serializes the views -> convert complex data (Djangio Python, objects) to more suitable form (JSON);
# similar to forms?
class EmployeeSerializer(serializers.ModelSerializer):
    # allow for info to be shown regarding the department (not just an ID, but also name)
    department = ShortDepartmentSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ('name', 'salary')

    def create(self, validated_data):

        # 'department': OrderedDict([('name': 'Finance')])
        department_name = validated_data.pop('department').get('name')
        department = Department.objects.get_or_create_department_by_name(department_name)

        return Employee.objects.create(
            **validated_data,
            department=department,
        )


# Custom serializers are rarely used
class TestSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    key = serializers.CharField()
    value = serializers.IntegerField()


class DemoSerialzer(serializers.Serializer):
    employees = ShortEmployeeSerializer(many=True)
    employees_count = serializers.IntegerField()
    departments = ShortDepartmentSerializer(many=True)
    first_department = serializers.CharField()
    most_populous_department = serializers.CharField()
