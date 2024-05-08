########################
# function Okuryazarligi
########################

# parameter, when we CREATE new function, function take a parameter.
# argument, when we CALL function, function take an argument.

print("a", "b")
print("a", "b", sep="__")
print("a", "b", sep="__", end=".")


########################
# initialize the function
########################


def calculate(input1):
    return input1 * 2


calculate(3)


def calculate(input1, input2):
    return input1 + input2


calculate(3, 4)


########################
# docstring - numpy and google options - setting in docstring
########################


def calculate(input1, input2):
    """
    Sum of two numbers

    :param input1:int
    :param input2:int
    :return:int
    """
    return input1 + input2


def say_hi(name):
    print("Hello " + name)


say_hi("Eftelya")

# take a value and returns a list

list_storage = []


def add_element(a, b):
    """
    take an element and add it to the list

    Parameters
    ----------
    a : int
    b : int

    """
    return list_storage.append(a * b)


add_element(18, 8)
print(list_storage)


# if curious about arguments of function, use command (?method_name) in python console


def calculate_air(warm, moisture, charge):
    """
    Calculates the air

    Parameters
    ----------
    warm : int
    moisture : int
    charge : int

    Returns
    -------
    tuple
    """
    warm = warm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (warm + moisture) / charge

    return warm, moisture, charge, output


warm, moisture, charge, output = calculate_air(98, 12, 78)


########################
# local and global variables
########################

# local -> in method
# global -> out of the method

###################################################################
# function conditions - loops


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(1032)


def number_check2(number):
    if number > 10:
        print("grater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")


number_check2(45)

# for loop

students = ["john", 'mark', 'vanessa', 'mariam']

for student in students:
    print(student.upper())

salaries = [100, 200, 300, 400, 500]

for salary in salaries:
    print(int(salary * 20 / 100 + salary))


def calculate_salary(salary, rate):
    return salary * rate / 100 + salary


calculate_salary(1500, 10)

salary_list = []

for salary in salaries:
    salary_list.append(int(calculate_salary(salary, 20)))

print(salary_list)


##########################################
# change the string:
# before : "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# start with upper case - start with lower case
# -- modunu al sifir olanlar upper case
# -- modunu al bir olanlar lower case
# if first letter uppercase, continue with lower case and the other condition occur vice versa.
# tek harfli ise lower case olarak kalacak


def alternating(name):
    new_string = ""
    for string_index in range(len(name)):
        if string_index % 2 == 0:
            new_string += name[string_index].upper()
        else:
            new_string += name[string_index].lower()
    return new_string


alternating("miuul")


#  The index() method returns the first occurrence of the specified value. If your string has repeated
#  letters, it will always return the index of the first occurrence, which might not be the current
#  letter’s index in the loop.

#   in this function, we iterate over the indices of the string rather than the characters themselves.
def snake_word_lower_upper(name):
    new_string = ""
    for s_index in range(len(name)):
        if s_index % 2 == 0:
            new_string += name[s_index].upper()
        else:
            new_string += name[s_index].lower()
    return new_string


snake_word_lower_upper("hi my name is john and i am learning python")

###############################################
# enumerate : allows you to iterate through a sequence and keep track of the index of each element
###############################################


A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

