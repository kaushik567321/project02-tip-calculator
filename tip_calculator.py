bill=float(input("what was the total bill?"))
num_of_people=int(input("how many people to split the bill? "))
tip= float(input("how much tip you want to give? "))
tip_as_percent= tip/100
total_tip_amount= bill*tip_as_percent
total_bill= bill+total_tip_amount
bill_per_person= total_bill/num_of_people
print(round(bill_per_person,2))