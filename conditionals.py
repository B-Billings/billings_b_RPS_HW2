temperature = int(input("input a value between 0 and 100: "))

if (temperature <= 4):
    print("water's state is solid")

elif (temperature < 100):
    print("water's state is liquid")

else:
    print("water is vapor")