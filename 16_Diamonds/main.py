"""Diamonds, by Al Sweigart
Draws diamonds of various sizes"""

def main():
    with open("diamonds.txt","w") as file:
        file.write("Diamonds, by Al Sweigart\n\n")

    #Display diamonds of sizes 0 through 6:
        for diamondSize in range(0,10):
            displayOutlineDiamond(diamondSize, file)
            file.write("\n")
            displayFilledDiamond(diamondSize, file)
            file.write("\n")

def displayOutlineDiamond(size, file):
    #Display the top half of the diamond
    for i in range(size):
        file.write(" " * (size - i - 1)) #Left side space
        file.write("/") #Left side of diamond
        file.write(" " * (i * 2)) #Interior of diamond
        file.write("\\\n") #Right side of diamond

    #Display the bottom part of the diamond
    for i in range(size):
        file.write(" " * i) #Left side space
        file.write("\\") #Left side of diamond
        file.write(" " * ((size - i - 1) * 2)) #Interior of diamond
        file.write("/\n") #Right side of diamond

def displayFilledDiamond(size, file):
    #Display the top half od the diamond
    for i in range(size):
        file.write(" " * (size - i - 1)) #Left side space
        file.write("/" * (i+1)) #Left half of diamond
        file.write("\\" * (i+1)) #Right half of diamond
        file.write("\n") #Newline

    #Display the bottom part of the diamond
    for i in range(size):
        file.write(" " * i) #Left side space
        file.write("\\" * (size - i)) #Left side of diamond
        file.write("/" * (size - i)) #Right side of diamond
        file.write("\n") #Newline

#If this program was run, run the game:
if __name__ == '__main__':
    main()
