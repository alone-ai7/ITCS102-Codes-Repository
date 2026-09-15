age = int(input ("Please enter your  age:  "))
is_employed = bool(input("Are you employed? (True/False): "))
credits = int(input("Please enter your credits score: "))
annual_income = int(input("Please enter your annual income: "))
has_collateral = bool(input("Do you have collateral? (True/False): "))

base_interest = 0.0

if  age >= 21 and is_employed == True:
    pass
    if credits >= 750:      #Tier one
        base_interest = 5.0
        if annual_income >= 100000:
            base_interest = 4.5
            print("Congratulations! You are approved for a loan of", base_interest, "%")
else:
    print("Rejected: Fails baseline criteria.")
 
if 600 <= credits < 750:                           #Tier two
    base_interest = 8.0
    
    if annual_income < 40000:
        risk_rate = 9.5
        print("Congratulations! You are approved for a loan of", risk_rate, "%")
    elif has_collateral == True:
        base_interest = 7.0
        print("Congratulations! You are approved for a loan of", base_interest, "%")
          
if credits < 600:                                                               #Tier three
    print("Rejected: Your credit score is too low.")
         
