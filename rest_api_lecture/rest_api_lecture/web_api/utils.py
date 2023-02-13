from rest_api_lecture.web_api.models import Department, Employee


# function used to (dynamically) return the Department with the most Employees
# could probably be done by some overlapping of the objects but ... :?
def get_most_populous_department():
    department_dict = {

    }

    departments = Department.objects.all()
    employees = Employee.objects.all()

    for department in departments:
        if not department in department_dict.keys():
            department_dict[department] = 0

    for employee in employees:
        current_dep = employee.department
        department_dict[current_dep] += 1

    max_department = max(department_dict, key=lambda x: department_dict[x])
    print(max_department)
    return max_department
