import sys
if len(sys.argv)=3:
  script_name=sys.argv[0]
  initial = float(sys.argv[1])
  deposit = float(sys.argv[2])
else:
   updated = initial + deposit

print(f"Initial Balance: {initial}")
print(f"Deposit Amount: {deposit}")
print(f"Updated Balance: {updated}")
