print("Welcome to PocketWise!")
print("Let's track your expenses!")
income = float(input("Enter your monthly income: "))
food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
shopping = float(input("Enter shopping expense: "))
miscellaneous = float(input("Enter miscellaneous expense: "))
others = float(input("Enter others expense: "))
total_expense = food+travel+shopping+miscellaneous+others
if total_expense > income:
    print("WARNING ⚠️: Your expenses exceed your income!")
    loss = total_expense - income
    print("Overspend Amount : ",loss)
else:
    remaining = income - total_expense
    savings_percent = (remaining / income) * 100
print("This is your Expense Report")
print("YOUR INCOME : ",income)
print("YOUR TOTAL EXPENSE : ",total_expense)
if total_expense < income:
    print("YOUR REMAINING AMOUNT : ",remaining)
    print("YOUR SAVING PERCENTAGE : ",round(savings_percent,2),"%")
else:
    print("No Remaining Amount")
if total_expense < income:
    if savings_percent >= 50:
        print("Excellent! You are saving really well!")
    elif savings_percent >= 30:
        print("Good job! But try to save a little more.")
    elif savings_percent >= 10:
        print("Better! But try more hard to save")
    else:
        print("Need to learn saving skills")
else:
    print("REDUCE EXPENSE")
print("Your Expense Breakdown Is :")
food_percentage = (food/total_expense)*100
print("Food Percentage : ",round(food_percentage,2),"%")
travel_percentage = (travel/total_expense)*100
print("Travel Percentage : ",round(travel_percentage,2),"%")
shopping_percentage = (shopping/total_expense)*100
print("Shopping Percentage : ",round(shopping_percentage,2),"%")
miscellaneous_percentage = (miscellaneous/total_expense)*100
print("Miscellaneous Percentage : ",round(miscellaneous_percentage,2),"%")
others_percentage = (others/total_expense)*100
print("Others Percentage : ",round(others_percentage,2),"%")
if food > travel and food > shopping and food > miscellaneous and food > others:
    print("You spend most on food : ",food)
elif travel > shopping and travel > miscellaneous and travel > others :
    print("You spend most in travel : ",travel)
elif shopping > miscellaneous and shopping > others:
    print("You spend most on shopping :",shopping)
elif miscellaneous > others:
    print("You spend most on miscellaneous :",miscellaneous)
else:
    print("You spend most on others : ",others)
print("So this is for this month keep tracking your Expense")
print("THANKYOUU")