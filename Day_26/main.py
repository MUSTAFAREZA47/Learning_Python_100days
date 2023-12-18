# ++++++++++++++++++++++++ list comprehension +++++++++++++++++++++++++++++++
number = [1, 2, 3, 4, 5]

# SYNTAX --->  new_number = [new_list for item in list if test]
new_number = [num + 5 for num in number]
# print(new_number)
name = "Ahmed"
letter_lists = [letter + "guru" for letter in name]
# print(letter_lists)
names = ["zen", "virat", "sanket", "jha", "zahir"]

short_name = [name for name in names if len(name) < 4]
# print(short_name)
long_name = [name.upper() for name in names if len(name) > 4]
# print(long_name)

numbers = [1, 1, 2, 3, 5, 8, 33, 21, 34, 55]
square_nums = [n * n for n in numbers]
# print(square_nums)

# input_num = input("give mix number to filter even number. ").split(",")
# print(input_num)
# int_number = [int(n) for n in input_num]
# even_num = [num for num in int_number if num % 2 != 0]
# print(even_num)

# common_number = [num for num in numbers if num not in int_number]
# print(common_number)

# for num in numbers:
#     for int_num in int_number:
#         if num == int_num:
#             print(num)


# +++++++++++++++++++++++++ Dictionary Comprehension +++++++++++++++++++
import random

student_name = ["zen", "virat", "sanket", "jha", "zahir"]

# SYNTAX --->  student_score = {key: value for item in list}
student_score = {student: random.randint(1, 100) for student in student_name}
# print(student_score)

# SYNTAX --->  high_score ={new_key: new_value for (key, value) in dict.items() if test}
high_score = {student: number for (student, number) in student_score.items() if number > 80}
# print(high_score)

# sentence = input("write any sentence to know words count. ").split(" ")

# words_count = {word: len(word) for word in sentence}
# print(words_count)

# looping through dictionary
for (key, value) in student_score.items():
    # print(key,value)
    pass

# looping through dataframes is same as dictionary but slight difference
import pandas

student_data = {
    "Name_student": ["zen", "virat", "sanket", "jha", "zahir"],
    "score": [125, 155, 145, 120, 130],
    "rating": [2, 5, 4, 1, 3]
}

# dct = {k: [v] for k, v in student_data.items()}

student_data_frames = pandas.DataFrame(student_data)
# print(student_data_frames)

# Loop through rows of a data frames
for (index, row) in student_data_frames.iterrows():
    print(row)
