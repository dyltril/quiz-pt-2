think = input("Hello! Would you like to add or subtract 2 numbers of your choice? ")
if think == "add":
    a = input("Choose a number. ")
    b = input("Choose another number to add with. ")
    sum = float(a) + float(b)
    print("Your sum is " + str(sum))
else:
    a = input("Choose a number. ")
    b = input("Choose another number to subtract with. ")
    diff = float(a) - float(b)
    print("Your difference is " + str(diff))
