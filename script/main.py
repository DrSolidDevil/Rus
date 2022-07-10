__author__ = ["DrSolidDevil"]
__copyright__ = "Copyright 2022, DrSolidDevil"
__credits__ = ["DrSolidDevil"]
__license__ = "GPL"
__version__ = "0.2"
__maintainer__ = ["DrSolidDevil"]

import funcs
import os

# These are settings variables
minimum_class_amount = 2
core = "{\n      \"intents\": [\n"



# These are container variables.
content = ""
tag_list = []
patterns_list = []
responses_list = []









# This is the input that determines how many times we will run the input loop aka how many classes
class_amount = int(input(f"""How many classes will this have? (minimum {minimum_class_amount})\n"""))

funcs.mca_check(class_amount, minimum_class_amount)

# Gives the option to output data to a file or print to terminal.
outputchoice = input("\nDo you want to output this to a file? (y/n)\n")


# Checks the output choice for errors and turns it to a boolean.
write_to_file = funcs.ocbool(outputchoice)


# Checks if the user wants to write to file, if so it requests a file name
if write_to_file is True:
    # Gets the name for the output file.
    filename = input("\nFilename: \nThis can be a already existing file that you want to be overwritten or a new file. ("
                     "don\'t write the file extension in the name)\n")

    # Gets the parent directory of this file.
    pardir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    # Adds the file extension to the file name
    filename = f"""{pardir}\\json\\{filename}.json"""
elif write_to_file is False:
    pass



# This just gives some info
print("\n( The separator for the sentences is the # symbol and leave no space for example: Hello#Hi = [\"Hello\",\"Hi\"] )")



# This adds all the inputs to a list that can later be fetched
for i in range(0, class_amount):
    tag = str(input("Tag name:\n"))
    a = str(input("Patterns:\n"))
    b = str(input("Responses:\n"))


    # Turns the string input into a list based on the # separator
    responses = a.split("#")
    patterns = b.split("#")

    # Adds the inputs to a list for the respective use
    tag_list.append(tag)
    patterns_list.append(patterns)
    responses_list.append(responses)


# Runs the inputs the amount of times that there are classes except one, the last one.
for i in range(0, class_amount):
    a = i - 1

    if i >= (class_amount - 1):
        break
    else:
        pass

    b = funcs.insertfm(tag_list[a], patterns_list[a], responses_list[a])

    content = content + b


# Runs the last input cycle.
lastinsert = funcs.insertlast(tag_list[(class_amount - 1)],
                              patterns_list[(class_amount - 1)],
                              responses_list[(class_amount - 1)])

# This adds the last class to the "file"
out = content+lastinsert
# This replaces the single quotation marks with double.
out = (core+out).replace("\'", "\"")


if write_to_file is True:
    f = open(filename, "w")
    f.write(out)
    print(f"""All data has been written to {filename}""")
elif write_to_file is False:
    print(out)
