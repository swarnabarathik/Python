employee_id=int(input("enter the employee id"))
basic_salary=int(input("enter the basic salary"))
allowance=int(input("enter the allowances"))
monthly_gross_salary=basic_salary+allowance
if(monthly_gross_salary>10000):
	income_tax=(20.0/100.0)*monthly_gross_salary
	net_salary=monthly_gross_salary-income_tax
	print("Net salary:%d"%income_tax)
else:
	net_salary=monthly_gross_salary
print("Employee id:%d"%employee_id)
print("Basic salary:%d"%basic_salary)
print("Aloowance:%d"%allowance)
print("gross pay:%d"%monthly_gross_salary)
print("Net pay:%d"%net_salary)
