def read_employees(file_name="employees_list.txt"):
    """
    Read Employees Function
    This function reads employee data from the text file and returns it.
    """
    employee_data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                employee_data.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return employee_data


def write_employees(employees_data, file_name="employees_list.txt"):
    """
    Write Employees Function
    This function writes employee data to the text file.
    """
    try:
        with open(file_name, 'w') as file:
            for employee in employees_data:
                file.write(employee + '\n')
        print(f"Employee data successfully written to '{file_name}'.")
    except Exception as e:
        print(f"Error: {e}")
