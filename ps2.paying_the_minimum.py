def monthly_interest_rate(annual_interest_rate):
    return annual_interest_rate / 12.0

def minimum_monthly_payment(previous_balance, minimum_monthly_payment_rate):
    return minimum_monthly_payment_rate * previous_balance

def monthly_unpaid_balance(previous_balance, minimum_monthly_payment):
    return previous_balance - minimum_monthly_payment

def updated_balance(monthly_unpaid_balance, monthly_interest_rate):
    return monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

total_paid = 0

for month in range(1, 13):
    rate = monthly_interest_rate(annualInterestRate)
    print("Month:"),
    print(month)

    min_payment = minimum_monthly_payment(balance, monthlyPaymentRate)
    print("Minimum monthly payment:"),
    print(round(min_payment, 2))

    balance = updated_balance(monthly_unpaid_balance(balance, min_payment), rate)
    print("Remaining balance:"),
    print(round(balance, 2))

    total_paid += min_payment

print("Total paid:"),
print(round(total_paid, 2))
print("Remaining balance:"),
print(round(balance, 2))
