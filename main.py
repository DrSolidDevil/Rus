__author__ = ["DrSolidDevil"]
__copyright__ = "Copyright 2022, DrSolidDevil"
__credits__ = ["DrSolidDevil"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = ["DrSolidDevil"]


# These are settings variables
minimum_class_amount = 2
core = "{\n      \"intents\": [\n"



# These are container variables.
content = ""
tag_list = []
patterns_list = []
responses_list = []




# This is used for turning lists of x and y data into a json class for all classes except the last one.
def insertFM(tag, patterns, responses):
    # Since we can't have brackets in a string.
    # If you want to use the format insert method so instead we also need to insert them.
    a = "                 {}\"tag\": \"{}\",\n                 \"patterns\": {},\n                 \"responses\" {}\n                 {},\n"

    a = a.format("{", tag, patterns, responses, "}")
    return a

# This is used for turning lists of x and y data into a json class but only for the last class.
def insertLast(tag, patterns, responses):
    # Since we can't have brackets in a string.
    # If you want to use the format insert method so instead we also need to insert them.
    a = "                 {}\n                 \"tag\": \"{}\",\n                 \"patterns\": {},\n                 \"responses\": {}\n                 {}\n            ]\n{}"
    a = a.format("{", tag, patterns, responses, "}", "}")
    return a




# This is the input that determines how many times we will run the input loop aka how many classes
class_amount = int(input(f"""How many classes will this have? (minimum {minimum_class_amount})\n"""))
# This just gives some info
print("The separator for the sentences is the # symbol and leave no space for example: Hello#Hi = [\"Hello\",\"Hi\"]")




# makes sure the amount of classes is able to be used without having an error.
if class_amount < minimum_class_amount:
    raise ValueError(f"""The amount of classes is below {minimum_class_amount}.""")
else:
    pass



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

    b = insertFM(tag_list[a], patterns_list[a], responses_list[a])

    content = content + b


# Runs the last input cycle.
lastinsert = insertLast(tag_list[(class_amount - 1)],
                              patterns_list[(class_amount - 1)],
                              responses_list[(class_amount - 1)])

# This adds the last class to the "file"
out = content+lastinsert
# This replaces the single quotation marks with double.
out = (core+out).replace("\'", "\"")


# Outputs the final product
print(out)
