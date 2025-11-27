import sys
if len(sys.argv) == 3:
    script_name=sys.argv[0]
    balance = float(sys.argv[1])
    deposit = float(sys.argv[2])
else:
    script_name=sys.argv[0]
    balance = 100
    deposit = 50
updated_balance = balance + deposit
print("Balance:", balance)
print("Deposit:", deposit)
print("Updated Balance:", updated_balance)
