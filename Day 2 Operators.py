def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent/100)*meal_cost
    tax = (tax_percent/100)*meal_cost
    total_cost = meal_cost+tip+tax
    
    print(round(total_cost))