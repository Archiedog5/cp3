def cough(func):

    def func_wrapper():
#stuff that happens before the function
        print("*Cough")
        func()

    #stuff that happens after the function
        print("*Cough")
    return func_wrapper


@cough
def awkward():
    print("Can I get a discount")

@cough
def answer():
    print("This is a dollar three. . .")

awkward()
answer()
