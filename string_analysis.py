#This is the file to analize the contents of the wordfile text file
#It creates a for loop and then iterates over the loop line by line
#Then it seperates the lines into different folders by conditional logic
import re

symbols_list = ["!", "@", "/", "$", "%", "^", "&", "*", "(", "#", ")"] #list for extra conditional logic
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  #list for extra conditional logic


title_count = 0
lower_count = 0
symbols_count = 0
uppers_count = 0
numbers_count = 0
everything_else_count = 0



def is_symbol(symbols):
    for s in symbols:
        return s

def is_number(numbers):
    for n in numbers:
        return n

wordlist = open("/root/Downloads/rockyou(1).txt", "r+")


title = open("/root/Desktop/password_analysis/title.txt", "w")
lower = open("/root/Desktop/password_analysis/lower.txt", "w")
symbols = open("/root/Desktop/password_analysis/symbols.txt", "w")
uppers = open("/root/Desktop/password_analysis/uppers.txt", "w")
numbers = open("/root/Desktop/password_analysis/numbers.txt", "w")
everything_else = open("/root/Desktop/password_analysis/everything_else.txt", "w")

for word in wordlist:

    if word.istitle():
        title.write(str(word) + "\n")
        title_count += 1

    elif re.search(r'\*\@\#\$\^\&', word):
        for word in wordlist:
            symbols.write(str(word) + "\n")
            symbols_count += 1

    elif word.isupper():
        uppers.write(str(word) + "\n")
        uppers_count += 1

    elif word.islower():
        lower.write(str(word) + "\n")
        lower_count += 1

    elif re.search(r'\d', word):
            for word in wordlist:
                    numbers.write(str(word) + "\n")
                    numbers_count += 1

else:
    everything_else.write(str(word) + "\n")
    everything_else_count += 1



wordlist.close()


title.close()
lower.close()
symbols.close()
uppers.close()
numbers.close()
everything_else.close()

print wordlist.closed


print lower.closed
print symbols.closed
print uppers.closed
print numbers.closed
print everything_else.closed



print title_count               #title alone
print lower_count               #lowers
print symbols_count             #symbols
print uppers_count              #uppers
print numbers_count             #numbers
print everything_else_count     #everthing else




