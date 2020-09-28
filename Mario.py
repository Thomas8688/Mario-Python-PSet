#========== Functions ==========#
#This function validates the input number by checking that it is an integer and that it is within the range 1-23
def validatenum(num):
#Checks if num is an integer
    try:
        num = int(num)
#Checks that num is more than zero
        if num > 0:
#Checks that num is less than 24
            if num <= 23:
                valid = True
            else:
                valid = False
        else:
            valid = False
    except:
        valid = False
    return valid


#This function completes the main objective of the task, given a number
def mario(validnum):
#Sets the size of the bottom layer
    basenum = validnum + 1
#The list that will be contain each layer as an item
    mario = []
#Adds the first layer to the list
    mario.append(basenum*'#')
#The loop that adds each layer, one by one
    for i in range(validnum-1):
        appender = []
        row = validnum-i
        hashes = row & '#'
        spaces = (basenum-row) * ' '
        appender.append(spaces)
        appender.append(hashes)
        appender = ''.join(appender)
        mario.append(appender)
    printer(mario[::-1])




#function that prints each item of the list on a new line
def printer(array):
    for element in array:
        print (element)

#========== Main Loop ==========#
#This is the main event loop
#This is the portion of the code which contains the user interface

cycle = True
while cycle:
    print ("Options:\n1 - Mario Design\n2 - Quit\n")
    runmario = input("Enter Option: ")
    runmarnum = validatenum(runmario)
    cont = True
    if runmarnum:
        if int(runmario) == 2:
            cycle = False
            cont = False

        elif int(runmario) != 1:
            cont = False
            print ("Invalid Input\n")
    else:
        cont = False
        print("Invalid Input\n")

    while cont:
        number = input("Enter a number between 1-23: ")
        validate = validatenum(number)
        if validate:
            number = int(number)
            print('\n')
            mario(number)
            print('\n')
            cont = False
        else:
            print("Invalid Input\n")
