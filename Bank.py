import sys
if len(sys.argv) == 3:
    balance = float(sys.argv[1])
    deposit = float(sys.argv[2])
else:
    balance = 100
    deposit = 50
updated_balance = balance + deposit
print("Updated Balance:", updated_balance)
