employee_id=int(input("enter the employee id"))
basic_salary=int(input("enter the basic salary"))
allowance=int(input("enter the allowances"))
monthly_gross_salary=basic_salary+allowance
if(monthly_gross_salary<=5000):
	net_salary=monthly_gross_salary
elif(monthly_gross_salary>=5001 and monthly_gross_salary<=10000):
	income_tax=(10/100)*monthly_gross_salary
	net_pay=monthly_gross_salary-income_tax
elif(monthly_gross_salary>=10001 and monthly_gross_salary<=20000):
	income_tax=(20/100)*monthly_gross_salary
	net_pay=monthly_gross_salary-income_tax
else:
	income_tax=(30.0/100.0)*monthly_gross_salary
	net_pay=monthly_gross_salary-income_tax
print("Employee id:%d"%employee_id)
print("Basic salary:%d"%basic_salary)
print("Allowance:%d"%allowance)
print("Monthly gross pay:%d"%monthly_gross_salary)
print("Income tax:%0.1f"%income_tax)
print("Net pay:%d"%net_pay)
