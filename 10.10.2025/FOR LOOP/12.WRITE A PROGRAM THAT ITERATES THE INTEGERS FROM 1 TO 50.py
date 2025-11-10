# Write a program that iterates the integers from 1 to 50
    # For Muliples of three print "Fizz" instead of the number
    # And for the multiples of five print "Buzz"
    # For numbers which are multiples of both three and five print "FizzBuzz"

for i in range (1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("                          FizzBuzz","(",i,")")
    else:
        if i % 5 == 0:
            print("             Buzz","(",i,")")
        else:
            if i % 3 == 0:
                print("Fizz","(",i,")")
    
