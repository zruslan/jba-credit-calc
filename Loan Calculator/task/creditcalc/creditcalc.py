import math

# write your code here

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
calc_type = input()

principal = ""
month_payment = ""
month_num = ""

if calc_type != "p":
    print("Enter the loan principal:")
    principal = int(input())

if calc_type != "a":
    print("Enter the annuity payment:")
    month_payment = float(input())

if calc_type != "n":
    print("Enter the number of periods:")
    month_num = int(input())

print("Enter the loan interest:")
interest = float(input()) / 100
monthly_i = interest / 12

if calc_type == "p":
    principal = round(month_payment
                      * ((1 + monthly_i) ** month_num - 1)
                      / (monthly_i * ((1 + monthly_i) ** month_num)))
    # Your loan principal = 800000!
    print("Your loan principal = {0}!".format(principal))

if calc_type == "a":
    month_payment = math.ceil(principal
                              * (monthly_i * ((1 + monthly_i) ** month_num))
                              / ((1 + monthly_i) ** month_num - 1))
    # Your monthly payment = 21248!
    print("Your monthly payment = {0}!".format(month_payment))

if calc_type == "n":
    month_num = math.ceil(math.log(month_payment
                                   / (month_payment - monthly_i * principal), 1 + monthly_i))
    # It will take 8 years and 2 months to repay this loan!
    years = int(month_num // 12)
    months = math.ceil(month_num % 12)
    parts = []
    if years:
        parts.append(str(years) + " year" + ('s' if years != 1 else ''))
    if months:
        parts.append(str(months) + " month" + ('s' if months != 1 else ''))
    period = " and ".join(parts)
    print("It will take {0} to repay this loan!".format(period))
