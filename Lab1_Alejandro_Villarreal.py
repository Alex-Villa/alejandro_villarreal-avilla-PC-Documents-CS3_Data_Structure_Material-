import hashlib

# This method is the file reader that opens the text documents and extracts the hash value of all users and saves them to a 2D array
def getUsers():
    try:
        with open("password_file.txt", "r") as text_file:
            users = []
            for line in text_file:
                line = line.rstrip()
                users.append(line.split(','))
        return users
    except FileNotFoundError:
        print("I'm sorry, but the file cannot be found.\n")
        print("Please place the file in the folder with the program and label it 'password_file' with .txt extension and start the program again.")
        quit()

# This method goes through the array and finds the hashed passwords that match the ones in the text file and returns the users password
def findMatch(num, users):
    for i in range(len(users)):
        numsalt = num + users[i][1]
        pwHash = hashlib.sha256(numsalt.encode('utf-8')).hexdigest()
        if pwHash == users[i][2]:
            return i
    return -1

# This method uses input form the user to go from the minimal string length till it reaches the max passing this info on to other method to generate the numbers
def numGenRecur(users, minStrLength, maxStrLength):
    if minStrLength <= maxStrLength:
        accounts = numGenerator(users, minStrLength)
        return accounts + numGenRecur(users, minStrLength + 1, maxStrLength)
    else:
        return []

# This method uses input form the parameter in order to use the right range for the loop as well as how many digits it is using told by the user
def numGenerator(users, numStringSize):
    numRangeSize = 10 ** numStringSize
    accounts = []
    for num in range(numRangeSize):
        num = str(num).zfill(numStringSize)
        pos = findMatch(num, users)
        if pos >= 0:
            accounts.append([users[pos][0], num])
    return accounts

# This is the main where input from the user is taken and passed to the other methods used in the program amd takes the arrays to print out the desired info
def main():
    # min value cannot be 0 or negative
    while True:  # This will loop forever
        minStrLength = int(input("Please enter the MINIMUM character length needed for a password: "))
        if (minStrLength > 0):  # when the input is more than 0
            break  # exit the infinite loop
        else:
            print("I'm sorry, but the minimum value can not be equal to or less than 0 it must be 1 or more.\n")

    # max value must be equal or greater then min value
    while True:
        maxStrLength = int(input("Please enter the MAXIMUM character length needed for a password: "))
        if (maxStrLength >= minStrLength):
            break
        else:
            print("I'm sorry, but your maximum must be more than or equal to your minimum value\n")

    print("Users can have a password with only", minStrLength, "to", maxStrLength, "characters.\n")
    print("Loading users data from archive file...\n")
    users = getUsers()
    print("Testing for passwords...")
    accounts = numGenRecur(users, minStrLength, maxStrLength)
    sortedAccounts = sorted(accounts, key=lambda l: int(l[0][4:]))
    print("Account  Password")
    for user in sortedAccounts:
        print("{:8s} {:8s}".format(user[0], user[1]))


main()