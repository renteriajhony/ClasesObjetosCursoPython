
class Employee:
    counter_employee: int = 0

    def __init__(self, name, department):
        Employee.counter_employee +=1
        self.id = Employee.counter_employee
        self.name = name
        self.department = department

    @classmethod
    def get_counter_employee(cls):
        """
        Returns the counter employee.
        :return: counter employee
        """
        return cls.counter_employee