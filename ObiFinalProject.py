'''Vehicle useful life calculator by Obi Idigo'''

'''A calculator designed to calculate the useful life of a vehicle dependent on user inputs. It can be used to quickly
estimate the trade offs between purchasing an Internal Combustion Engine Vehicle (ICE) and an Electric Vehicle (EV).'''


# Define Constants. Constant please do not change while script is running!

EV_USE_CYCLE = 300000 # Estimated use cycle of Electric Vehicles in miles.

ICE_USE_CYCLE = 200000 # Estimated use cycle of Internal Combustion Engine Vehicle in miles.

MILEAGE_RATE = .58 # IRS cost to operate a vehicle per mile.


# Define functions

def currentmileage(cm):
    while True:
        try:
            cm = int(cm)
            print(cm)
            return cm

        except Exception as e:
            print("\nPlease enter numbers only! NO letters or decimals!")
            print("\n\t\t\t", e)
            cm = input("What is your current vehicle mileage? ")
            continue


def annualmileage(an):
    while True:
        try:
            an = int(an)
            print(an)
            return an
        except Exception as e:
            print("\nPlease enter numbers only! NO letters or decimals!")
            print("\n\t\t\t", e)
            an = input("How many miles a year do you put or plan on putting on your vehicle? ")
            continue


def totalpurchaseprice(tp):
    while True:
        try:
            tp = int(tp)
            print(tp)
            return tp
        except Exception as e:
            print("\nPlease enter numbers only! NO letters or decimals!")
            print("\n\t\t\t", e)
            tp = input("What was the total price you paid for your vehicle after taxes and fees? ")
            continue


def salvagevalue(sv):
    while True:
        try:
            sv = int(sv)
            print(sv)
            return sv
        except Exception as e:
            print("\nPlease enter numbers only! NO letters or decimals!")
            print("\n\t\t\t", e)
            sv = input("How much do you think you will get for you car when you finally sell it? ")
            continue


def vehiclemake(v_make):
    while True:
        try:
            v_make = str(v_make).title()
            print(v_make)
            return v_make
        except Exception as e:
            print("\n\t\t\t", e)
            v_make = input("\nWhat is the make of your car? ").title()
            continue


def vehiclemodel(v_model):
    while True:
        try:
            v_model = str(v_model).title()
            print(v_model)
            return v_model
        except Exception as e:
            print("\n\t\t\t", e)
            v_model = input("\nWhat is the model of your car? ").title()
            continue


def vehiclemodelyear(v_year):
    while True:
        try:
            v_year = int(v_year)
            print(v_year)
            return v_year
        except Exception as e:
            print("\nPlease enter numbers only! NO letters or decimals!")
            print("\n\t\t\t", e)
            v_year = input("\nWhat is the model year of your car? ")


# Perform calculations and print outputs.
def evusefullife(cm,an):
    Ev_useful_life = (EV_USE_CYCLE - cm) / an
    print("\nThe estimated useful life of your car if it is an Electric Vehicle is:",round(Ev_useful_life,1),"years")
    return Ev_useful_life

def iceusefullife(cm,an):
    Ice_useful_life = (ICE_USE_CYCLE - cm) / an
    print("\nThe estimated useful life of your car if it is an Internal Combustion vehicle is:",round(Ice_useful_life,1),"years.")
    return Ice_useful_life


# Calculate straight line depreciation expense.
def evdepreciationexpense(tp,sv,ev):
    EV_depreciation_expense = (tp - sv) / ev # Formula for straight line depreciation
    print("\nEV Deprecation = $",round(EV_depreciation_expense,2),"every year")
    return EV_depreciation_expense

def icedepreciationexpense(tp,sv,ice):
    ICE_depreciation_expense = (tp - sv) / ice # Formula for straight line depreciation
    print("\nInternal Combustion Depreciation = $",round(ICE_depreciation_expense,2),"every year")
    return ICE_depreciation_expense


# Main Program

# Collect inputs from user.
v_make = vehiclemake(input("\nWhat is the make of your car? ").title())

v_model = vehiclemodel(input("\nWhat is the model of your car? ").title())

v_year = vehiclemodelyear(input("\nWhat is the model year of your car? "))

cm = currentmileage(input("\nWhat is your current vehicle mileage? "))

an = annualmileage(input("\nHow many miles a year do you put or plan on putting on your vehicle? "))

tp = totalpurchaseprice(input("\nWhat was the total price you paid for your vehicle after taxes and fees? "))

sv = salvagevalue(input("\nHow much do you think you will get for you car when you finally sell it? "))

print("\n")



# Display list and dictionary of inputs.
# Create list of headers
my_vehicle_list_header = ["Vehicle Make", "Vehicle Model", "Vehicle Year", "Current Mileage", "Annual Mileage", "Total Purchase Price", "Salvage Value", "EV Useful Life", "ICE Useful Life"]
print(my_vehicle_list_header)

# Create list of inputs about vehicle
my_vehicle_list = [v_make,v_model,v_year,cm,an,tp,sv,evusefullife(cm,an),iceusefullife(cm,an)]
print(my_vehicle_list)

# Create vehicle tuple by zipping together the list of headers and list of inputs
my_vehicle_tuple = list(zip(my_vehicle_list_header,my_vehicle_list))
print(my_vehicle_tuple)

# Turn vehicle tuple into a vehicle dictionary
my_vehicle_dict = dict(my_vehicle_tuple)
print(my_vehicle_dict)


# Print out sentences with useful calculations from the users input
ev = evusefullife(cm,an)

ice = iceusefullife(cm,an)

evdepreciationexpense(tp,sv,ev)

icedepreciationexpense(tp,sv,ice)


# Create functions of menu options.
def savetofile(my_vehicle_dict):
    with open("MyVehicles.txt", "a") as f:
        for header, value in my_vehicle_dict.items():
            f.write("{},{}\n".format(header,value))
    print("\nInputs saved to file!")

def readfromfile():
    with open("MyVehicles.txt", "r+") as f:
        read_file = f.read()
        print(read_file)

def addnewvehicle():
    # Collect inputs from user.
    v_make = vehiclemake(input("\nWhat is the make of your car? ").title())

    v_model = vehiclemodel(input("\nWhat is the model of your car? ").title())

    v_year = vehiclemodelyear(input("\nWhat is the model year of your car? "))

    cm = currentmileage(input("\nWhat is your current vehicle mileage? "))

    an = annualmileage(input("\nHow many miles a year do you put or plan on putting on your vehicle? "))

    tp = totalpurchaseprice(input("\nWhat was the total price you paid for your vehicle after taxes and fees? "))

    sv = salvagevalue(input("\nHow much do you think you will get for you car when you finally sell it? "))

    print("\n")

    # Display list and dictionary of inputs.
    # Create list of headers
    my_vehicle_list_header = ["Vehicle Make", "Vehicle Model", "Vehicle Year", "Current Mileage", "Annual Mileage",
                              "Total Purchase Price", "Salvage Value", "EV Useful Life", "ICE Useful Life"]
    print(my_vehicle_list_header)

    # Create list of inputs about vehicle
    my_vehicle_list = [v_make, v_model, v_year, cm, an, tp, sv, evusefullife(cm, an), iceusefullife(cm, an)]
    print(my_vehicle_list)

    # Create vehicle tuple by zipping together the list of headers and list of inputs
    my_vehicle_tuple = list(zip(my_vehicle_list_header, my_vehicle_list))
    print(my_vehicle_tuple)

    # Turn vehicle tuple into a vehicle dictionary
    my_vehicle_dict = dict(my_vehicle_tuple)
    print(my_vehicle_dict)

    # Print out sentences with useful calculations from the users input
    ev = evusefullife(cm, an)

    ice = iceusefullife(cm, an)

    evdepreciationexpense(tp, sv, ev)

    icedepreciationexpense(tp, sv, ice)

    savetofile(my_vehicle_dict)


# Main Menu

while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a vehicle
    3) Save Data to File
    4) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    if (strChoice.strip() == '1'):
        readfromfile()

    elif (strChoice == '2'):
        addnewvehicle()

    elif (strChoice == '3'):
        # Save inputs to file
        savetofile(my_vehicle_dict)

    elif (strChoice.strip() == '4'):
        # Exit the program
        break
