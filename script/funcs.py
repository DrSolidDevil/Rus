__author__ = ["DrSolidDevil"]
__copyright__ = "Copyright 2022, DrSolidDevil"
__credits__ = ["DrSolidDevil"]
__license__ = "GPL"
__version__ = "0.3"
__maintainer__ = ["DrSolidDevil"]




def insertfm(tag, patterns, responses):
    """
    This is used for turning lists of x and y data into a json class for all classes except the last one.

    :param tag:
    :type tag: str
    :param patterns:
    :type patterns: list
    :param responses:
    :type responses: list
    :return: JSON Class in string.
    """
    # Since we can't have brackets in a string.
    # If you want to use the format insert method so instead we also need to insert them.
    a = "                 {}\"tag\": \"{}\",\n                 \"patterns\": {},\n                 \"responses\": {}\n                 {},\n"

    a = a.format("{", tag, patterns, responses, "}")
    return a


def insertlast(tag, patterns, responses):
    """
    This is used for turning lists of x and y data into a json class but only for the last class.

    :param tag:
    :type tag: str
    :param patterns:
    :type patterns: list
    :param responses:
    :type responses: list
    :return: JSON Class in string.
    """
    # Since we can't have brackets in a string.
    # If you want to use the format insert method so instead we also need to insert them.
    a = "                 {}\n                 \"tag\": \"{}\",\n                 \"patterns\": {},\n                 \"responses\": {}\n                 {}\n            ]\n{}"
    a = a.format("{", tag, patterns, responses, "}", "}")
    return a



def mca_check(ca, mca):
    """
    This function checks that the amount of classes is equal or more to the minimum.

    :param ca: The amount of classes that will be made.
    :type ca: int
    :param mca: The minimum amount of classes for this script to work.
    :type mca: int
    :return: None
    """

    # makes sure the amount of classes is able to be used without having an error.
    if ca < mca:
        raise Exception(f"""The amount of classes is below {mca}.""")



def ocbool(oc):
    """
    Checks the output choice for errors and turns it to a boolean.

    :param oc: The way the data will be outputted (file or print)
    :type oc: str
    :return: The boolean value of the oc.
    """

    # This just formats the input so that capital and extra spaces work
    oc.replace(" ", "")
    oc.lower()

    # Turns yes or no (y/n) to a boolean value.
    if oc == "y":
        a = True
    elif oc == "n":
        a = False

    return a
