#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.

def total_calc(bill_amount,tip_amount):
    total=bill_amount*(1+0.01*tip_amount)
    total=round(total,2)
    print(f"please pay {total}")
    
total_calc(12,2)