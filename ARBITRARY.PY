def Operation_Of(*args,**kargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for val in kargs.values():
        print(val)
Operation_Of("We","learning","Pyuthon",name="pattabhi",year="4Th year", degree = "BE ECE")