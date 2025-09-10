# Python weight Converter
try:
    weight = float(input("Enter Your weight: "))
    unit = input("Kilograms or pound ? (K or L): ").strip().upper()

    if unit == "K":
        weight = weight* 2.205
        unit = "lbs."
        #print(f"Your weight is: {round(weight, 2)} {unit}")
    elif unit =="L":
        weight = weight / 2.205
        unit ="kgs."
        #print(f"Your weight is: {round(weight, 2)} {unit}")
    else:
        print(f"{unit} was not valid")
        exit()  # Exit the program if the input is invalid.

    print(f"Your weight is: {round(weight,2)} {unit}")

except ValueError:
    print("Invalid input! Please enter a numerical value for weight.")


