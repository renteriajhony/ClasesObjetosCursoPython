from system_employees_company.company import Company
from system_employees_company.employee import Employee

print('*** Sistema de empleados ***')

# Create company
company1 = Company('Udemy')
company2 = Company('Global Mentory')

#Hire Employee
# Company 1
company1.hire_employee('Juan', 'Ventas')
company1.hire_employee('Maria', 'Marketing')
company1.hire_employee('Pedro', 'Ventas')
company1.hire_employee('Ana', 'Recursos Humanos')
# Company 2
company2.hire_employee('Michel', 'Ventas')
company2.hire_employee('Paul', 'Ventas')

# Get total employees
print(f''' Numero de empleados creados
    Total: {Employee.get_counter_employee()}
''')

# Get total employess for departament
employes_for_departament = company1.get_employees_number_for_departament('Ventas')
print(f''' Numero de empleados en ventas
    Total: {employes_for_departament}
''')

#Get employees
company2.get_total_employees()