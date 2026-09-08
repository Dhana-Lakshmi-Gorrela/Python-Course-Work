Registered = input("Registered (True/false): ")
fee_paid = input("Fee paid (True/False): ")

if Registered == "True":
    if fee_paid == "True":
        print("Tournment Entry confirmed")

    else:
            print("Entry Free Pending")
else:
        print("Registration Requried")
    

