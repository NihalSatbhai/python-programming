def hello_world(name):
    print(f'Hi {name}')
hello_world('Nihal')


def return_example(num1,num2):
    return num1+num2
result = return_example(10,20)
print(result)


work_hours = [('Neha', 200), ('Vaibhavi', 250), ('Nihal', 400)]
def tuple_unpacking(work_hours):
    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    
    return(employee_of_the_month,current_max)

result = tuple_unpacking(work_hours)
print(result)