year = input("Enter thr year: ")

if int(year) % 4 == 0:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            print("{0} is leap".format(year))
        else:
            print(("{0} is not leap".format(year)))
    else:
        print(("{0} is leap".format(year)))
else:
    print(("{0} is not leap".format(year)))