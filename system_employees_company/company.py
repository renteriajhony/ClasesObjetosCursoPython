from system_employees_company.employee import Employee

class Company:

    def __init__(self, name: str,):
        self.name = name
        self.employees_company: list[Employee] = []

    def hire_employee(self, name, departament):
        employee = Employee(name, departament)
        self.employees_company.append(employee)

    def get_employees_number_for_departament(self, departament: str) -> int :
        counter_employee_for_departament = 0
        for employee in self.employees_company:
            if employee.department == departament:
                counter_employee_for_departament += 1

        return counter_employee_for_departament

    def get_total_employees(self) :
        for employee in self.employees_company:
            print(f''' Empleado {employee.id}
            Name: {employee.name}
            Department: {employee.department}
            ''')