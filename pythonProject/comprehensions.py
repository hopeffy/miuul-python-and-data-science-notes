import seaborn as sns

##################################
# list comprehension
###################################

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(salary):
    return salary * 0.2 + salary


null_list = []

for s_salary in salaries:
    if s_salary > 3000:
        null_list.append(new_salary(s_salary))
    else:
        null_list.append(new_salary(s_salary * 2))

[new_salary(s_salary * 2) if s_salary < 3000 else new_salary(s_salary) for s_salary in salaries]

[salary * 2 for salary in salaries]

# if condition exists has without else, write on the right side
# although with else write on the left side of the for-conditions.

[salary * 2 for salary in salaries if salary < 4000]

[salary * 2 if salary < 4000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 4000 else new_salary(salary) * 0 for salary in salaries]

students = ["John", "Smith", "Mark", "Mariam"]

students_no = ["John", "Mark"]

# two different way to select student on the list student_no.
[student.lower() if students_no.__contains__(student) else student.upper() for student in students]

[student.lower() if student in students_no else student.upper() for student in students]

# not in structure
[student.upper() if student not in students_no else student.lower() for student in students]

##################################
# dictionary comprehensions
###################################

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}

#######################################################
# Application Question
########################################################

# purpose : square of the even numbers will be added in dictionary

numbers = range(10)
dict = {1: 1, 2: 1, 3: 1, 4: 1}

{k: k ** 2 for (k, v) in dict.items() if k % 2 == 0}

{n: n ** 2 for n in numbers if n % 2 == 0}

#######################################################
# List & Dict Comprehension Applications
########################################################

#######################################################
# change the name of variables of the dataset
########################################################

# before: ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_previous', 'ins_losses', 'abbrev']

# after : ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# import seaborn as sns (in the top of the file)

df = sns.load_dataset("car_crashes")

# to reach column names of the data frame
df.columns

df.columns = [column.upper() for column in df.columns]

#######################################################
# add FLAG to the beginning of the name of variables in dataset if the name contains "INS" otherwise add NO_FLAG
########################################################

df.columns = ["FLAG_" + col if "INS" in col else "NOT_FLAG_" + col for col in df.columns]

#######################################################
# purpose : key: string, value: list --> create a dictionary
# just numerical values
########################################################

# output =:
# {'total' : ['mean', 'min', 'max', 'var'],
# 'speeding' : ['mean', 'min', 'max', 'var'] ... }

df.columns
# O refers to object. datatype != object (string)
num_cols = [col for col in df.columns if df[col].dtype != 'O']

v = ['mean', 'min', 'max', 'var']

# long way
dict = {}
for col in num_cols:
    dict[col] = v

# short way
new_dict = {col: v for col in num_cols}

df[num_cols].head()
# every variable if has the same variable with data frame agg function return understand what will you want
# istedigim fonksiyonlari sozlugun icerisindeki degiskenler burada df'de varsa bunlari key degeri olarak tutar,
# bu fonksiyonlari gidip butun degiskenlere otomatik olarak uygular.
df[num_cols].agg(new_dict)