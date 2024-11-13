#Exceptions is how we deal with errors created by users that doesn't break to code.
#Errors to fix are dividning by zero, file not found error, value error, type error, and index error.
 #finally: is a way to make sure something always happens at the end of the loop.   
class NegativeNumberError(Exception):
    pass

while True:

    try:
        num = int(input("Tell me a number: "))

    except (ValueError, TypeError):
        print("That wasn't an integer you specail child")
        continue
    
    else:
        break

while True:

    try:
        numTwo = int(input("Tell me another number: "))
        if numTwo <= 0:
            raise NegativeNumberError("Can't be a negative number.")

    except ValueError:
        print("That wasn't an integer you specail child")
        continue

    except NegativeNumberError as e:
        print(e)
    
    else:
        try:
            print(f'{str(num)} divided {str(numTwo)} equals {num/numTwo}')
            break

        except ZeroDivisionError:
            print("You can't divide by 0, try again")
            continue
   
    finally: 
        print("You are a mistake.")
        