# Calculate the net yearly/monthly/weekly/daily salary based on Tax code/ student loan/ Pension
# print welcome sentence
print("Welcome to the UK salary calculator_v1.0\n")

#input annual gross salary
annualGrossSalary = int (input ('Please type in your annual salary without "£": \n'))

#input pension percentage and calculate taxable salary
pensionRate = float (input ("How many percentage do you contribute to your pension? (please type in deciaml format, 1% = 0.01)\n"))
pensionAmount = annualGrossSalary * pensionRate
print(f"Your annual pension is £{pensionAmount}\n")

#input Tax Code and extract the personal allowance
# if the salary above allowance <= 37,700, 20% tax; >37,700 and <= 150,000, 40%; else 45%
taxCode = input("Please type in your Tax Code: ")
personalAllowance = int (taxCode [:-1]) * 10
taxableSalary = annualGrossSalary - pensionAmount
allowanceDifference = taxableSalary - personalAllowance
if allowanceDifference <= 37700:
    tax = allowanceDifference * 0.2
elif allowanceDifference <= 150000:
    tax = 37700 * 0.2 + (allowanceDifference - 37700) * 0.4
else: tax = 37700 * 0.2 + (15000 - 37700) * 0.4 + (allowanceDifference - 15000) * 0.45
print(f"Your annual tax is £{tax}\n")

#NI payment: exclude pension, classify by weekly salary.
#if weekly salary <= 184, no NI; if >184 and <= 967, pay 12% of gross non-pension salary
taxableWeeklySalary = taxableSalary / 52
if taxableWeeklySalary <= 184:
    NIamount = 0
elif taxableWeeklySalary <= 967:
    NIamount = (taxableWeeklySalary - 184) * 0.12 * 52
else:
    NIamount = (967 * 0.12 + (taxableWeeklySalary - 967) * 0.12) * 52
print(f"Your annual National Insurance payment is £{round(NIamount,2)}\n")

#Student loan, for student in England, plan 2 is applicable: taxable salary > 27295, pay 9%.
if taxableSalary <= 27295:
    studentLoan = 0
else:
    studentLoan = (taxableSalary - 27295) * 0.09
print(f"Your annual student loan payment is £{round(studentLoan,2)}\n")

#Display the net salary
annualNetSalary = annualGrossSalary - pensionAmount - tax - NIamount - studentLoan
print(f"Your annual net salary is £{round(annualNetSalary,2)}\n"
      f"Your monthly net salary is £{round((annualNetSalary/12),2)}\n"
      f"Your weekly net salary is £{round((annualNetSalary/52),2)}\n"
      f"Your daily net salary is £{round((annualNetSalary/365),2)}\n")
