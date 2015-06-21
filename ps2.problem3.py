monthly_interest_rate = annualInterestRate / 12.0
payment_lower_bound = balance / 12.0
payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0

def unpaid_balance(previous_balance, monthly_payment):
    return previous_balance - monthly_payment

def updated_balance(unpaid_balance, monthly_interest_rate):
    return unpaid_balance + (monthly_interest_rate * unpaid_balance)

lowest_payment = (payment_lower_bound + payment_upper_bound) / 2.0
last_lowest = None

while True:
    remaining = balance
    months = 0

    while remaining > 0:
        unpaid = unpaid_balance(remaining, lowest_payment)
        remaining = updated_balance(unpaid, monthly_interest_rate)
        months += 1
        if months > 12:
            payment_lower_bound = lowest_payment
            break
        if remaining < 0:
            payment_upper_bound = lowest_payment
            break

    if last_lowest == lowest_payment:
        break

    last_lowest = lowest_payment
    lowest_payment = (payment_lower_bound + payment_upper_bound) / 2.0

print("Lowest Payment:"),
print(round(lowest_payment, 2))

