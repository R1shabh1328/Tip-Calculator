print("welcome to tip calc!")
bill = input("total bill?\n")
tip = input("tip?\n")
split = input("no.of ppl?\n")

float_bill = float(bill)
float_tip = float(tip)
int_split = int(split)

tip_percent = (float_tip/100)

final_bill = (float_bill * tip_percent + float_bill)

bill_per_person = (final_bill/int_split)

print(f"your bill is {bill_per_person}")
