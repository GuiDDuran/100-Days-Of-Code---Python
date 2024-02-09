# Functions with outputs.
def format_name01(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name01("GuiLHERme", "dURan"))


# Functions with multiple return values.
def format_name02(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name02(input("What's your first name? "), input("What's your last name? ")))


def format_name03(f_name, l_name):
    """"Take a first and last name and format it to return thr title case version of the name"""  # It's a Docstring, it's used to improve the code documentation, and has to be right down the function's definition.
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name03(input("What's your first name? "), input("What's your last name? ")))


