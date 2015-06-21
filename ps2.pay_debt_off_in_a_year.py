# Test Case 1:
# balance = 3329
# annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

# Test Case 2:
# balance = 4773
# annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 440

# Test Case 3:
# balance = 3926
# annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 360

monthly_interest_rate = annualInterestRate / 12.0

def unpaid_balance(previous_balance, monthly_payment):
    return previous_balance - monthly_payment

def updated_balance(unpaid_balance, monthly_interest_rate):
    return unpaid_balance + (monthly_interest_rate * unpaid_balance)

lowest_payment = 10

while True:
    remaining = balance
    months = 0

    while remaining > 0:
        unpaid = unpaid_balance(remaining, lowest_payment)
        remaining = updated_balance(unpaid, monthly_interest_rate)
        months += 1
        if months > 12:
            break

    if months <= 12:
        break
    else:
        lowest_payment += 10

print("Lowest Payment:"),
print(lowest_payment)
