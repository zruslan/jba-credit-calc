import math
import argparse
import sys


# write your code here
parser = argparse.ArgumentParser()

# choices=["diff", "annuity"]
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if ((args.type not in ("annuity", "diff")) or
        (args.type == "diff" and args.payment) or
        (not args.interest) or
        (len(sys.argv) != 5) or
        (args.payment and float(args.payment) < 0) or
        (args.principal and int(args.principal) < 0) or
        (args.periods and int(args.periods) < 0) or
        (args.interest and float(args.interest) < 0)):
    print("Incorrect parameters")
    exit()

calc_type = ""
principal = ""
month_payment = ""
month_num = ""

if args.principal:
    principal = int(args.principal)
else:
    calc_type = "p"

if args.payment:
    month_payment = float(args.payment)
else:
    calc_type = args.type  # 2 variants: diff and annuity

if args.periods:
    month_num = int(args.periods)
else:
    calc_type = "n"

interest = float(args.interest) / 100
monthly_i = interest / 12

if calc_type == "p":
    principal = math.floor(month_payment
                           * ((1 + monthly_i) ** month_num - 1)
                           / (monthly_i * ((1 + monthly_i) ** month_num)))
    # Your loan principal = 800000!
    print("Your loan principal = {0}!".format(principal))

if calc_type == "annuity":
    month_payment = math.ceil(principal
                              * (monthly_i * ((1 + monthly_i) ** month_num))
                              / ((1 + monthly_i) ** month_num - 1))
    # Your monthly payment = 21248!
    print("Your annuity payment = {0}!".format(month_payment))

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

if calc_type == "diff":
    total_pay = 0
    for x in range(1, month_num + 1):
        month_payment = math.ceil(principal / month_num + monthly_i * (principal - principal * (x - 1) / month_num))
        print("Month {0}: payment is {1}".format(x, month_payment))
        total_pay += month_payment
    print("")
else:
    total_pay = int(month_num * month_payment)

# Overpayment = 45837
print("Overpayment = {}".format(total_pay - principal))
