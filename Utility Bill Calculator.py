# A program to calculate customers monthly utility bill with GGE

month_fee = 120.62   # fixed monthly fee every GGE customer pays
gas_fee = 1.32      # fixed monthly trascaction fee every natura gas customer is charged to offset GGE's industry leading network

account = str(input("Enter your account number"))
month = str(input("Enter the Month number [For January enter 1]"))

# Indicates which province user is in. GGE is required to charge customers the tax rate depending on the province they are in

province = input("Enter your province or territory in abbreviated form [Example: Alberta = AB]")
if province == "AB" or "BC" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT":
    result = 0.05
elif province == "ON":
    result = 0.15
elif province == "NB" or "NL" or "NS" or "PE":
    result =  0.13

# in addition to the fixed monhtly fees; customer are billed for their usage of electricty based on the type of plan they are enrolled in

elec_usage = int(input("Enter your electricty usage this month in kWh"))

elec_plan = (input("What is your current electiry plan [EFIR or EFLR]"))
if elec_plan == "EFIR":
    if elec_usage <= 1000: 
        elec_rate = elec_usage * 0.0836
    else: 
        elec_rate = 1000 * 0.0836 + ((elec_usage - 1000) * 0.0941)
elif elec_plan == "EFLR":
        elec_rate = elec_usage * 0.0911

# in addition to the fixed monhtly fees; customer are billed for their usage of gas based on the type of plan they are enrolled in

gas_usage = int(input("Enter your Gas usage this month in GJ "))

gas_plan = (input("What is your current natural gas plan [GFIR or GFLR]"))
if gas_plan == "GFIR":
    if gas_usage <= 950: 
        gas_rate = gas_usage * 0.0456
    else: 
        gas_rate = 950 * 0.0456 + ((gas_usage - 950) * 0.0589)
elif gas_plan == "GFLR":
        gas_rate = gas_usage * 0.0393


#calculates the sales tax based on the monthly bill

tax_amount = (elec_rate + gas_rate + month_fee + gas_fee) * result

# this reflects the total monthly bill for the cusomter; including all fees, taxes, plans and usage. 

total_bill = elec_rate + gas_rate + month_fee + gas_fee + tax_amount

# prints the total to the user and ends program

print("Thank you, your total amount due now is; CDN$ ", round(total_bill, 2))