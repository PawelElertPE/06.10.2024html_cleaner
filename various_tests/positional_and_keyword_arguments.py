def create_employee_record(employee_id, name, salary, department, active, committees):
  """Creates a new employee record.

  Args:
    employee_id: The unique identifier for the employee.
    name: The employee's full name.
    salary: The employee's annual salary.
    department: The department the employee belongs to.
    active: Indicates whether the employee is currently active (True) or inactive (False).
    committees: A list of committees the employee is a member of.

  Returns:
    A dictionary representing the new employee record.
  """

#   employee_record = {
#       "employee_id": employee_id,
#       "name": name,
#       "salary": salary,
#       "department": department,
#       "active": active,
#       "committees": committees
#   }

#   return employee_record

# jackson_record = create_employee_record(
#     101, "Jackson Thodey", 89000, "Sales", True, ["Promotions", "Diversity and Inclusion"]
# )

# jackson_record


def create_employee_record(
    employee_id: int, 
    name: str, 
    salary: float,
    department: str, 
    active: bool, 
    committees: list[str]
    ) -> dict:
  """Creates a new employee record.

  Args:
    employee_id: The unique identifier for the employee (integer).
    name: The employee's full name (string).
    salary: The employee's annual salary (float).
    department: The department the employee belongs to (string).
    active: Indicates whether the employee is currently active (boolean).
    committees: A list of committees the employee is a member of (list of strings).

  Returns:
    A dictionary representing the new employee record.
  """

  employee_record = {
      "employee_id": employee_id,
      "name": name,
      "salary": salary,
      "department": department,
      "active": active,
      "committees": committees
  }

  return employee_record

lara_record = create_employee_record(
    employee_id= 102,
    name= "Lara Croft",
    salary= 96000,
    department= "Operations",
    active= False,
    committees =['Cultural']
)

print(lara_record)