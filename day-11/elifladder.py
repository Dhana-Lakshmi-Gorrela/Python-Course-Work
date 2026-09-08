budget = int(input("Enter the budget: "))

if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("resort stay")
elif budget > 3000:
    print("movie and dinner")
elif budget > 1000:
    print("cafe and shopping")
elif budget > 500:
    print("street food and park visit")
else:
    print("stay home")
    
    
