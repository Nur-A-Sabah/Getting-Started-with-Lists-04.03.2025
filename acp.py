def numbers(beginning, ending):
    for j in range(beginning, ending +1):
        y = j*j
        if y % 2 == 0:
            print(f"The number is : {j} , the squre of the number is: {y} and this is an even number")
        else:
             print(f"The number is : {j} , the squre of the number is: {y} and this is an odd number")
beginning = int(input("enter the starting number: "))
ending = int(input("enter the ending number: "))

numbers(beginning , ending)