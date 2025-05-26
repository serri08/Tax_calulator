# salary calculator (mini project ) with percentage
basic_salary= float(input("enter the basic salary"))
bonus_per=float(input("enter the bonus in percentage"))
bonus_val= basic_salary*bonus_per/100
deductions_per = float(input("enter deductions percentage"))
deductions_value = basic_salary*deductions_per/100

final_salary = basic_salary +bonus_val -deductions_value

print("basic salary is....",basic_salary)
print("bonus value is .....",bonus_val)
print("deduction value is .....",deductions_value)
print("final salary is....",final_salary)


