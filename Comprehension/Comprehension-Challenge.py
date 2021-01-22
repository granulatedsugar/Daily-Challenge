# Daily Challenge : List Comprehension & Dict Comprehension
# Challenge 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_numbers = [n**2 for n in numbers]

print(new_numbers)

#%%
# Challenge 2
evens = [n for n in numbers if n % 2 == 0]

print(evens)

# %%
# Challenge 3
"""
Instructions
Take a look inside file1.txt and file2.txt. They each contain a
bunch of numbers, each number on a new line.

You are going to create a list called result which contains the
numbers that are common in both files.
"""
with open("file1.txt", mode='r') as file1:
    Lines1 = [line.rstrip() for line in file1.readlines()]

with open("file2.txt", mode='r') as file2:
    Lines2 = [line.rstrip() for line in file2.readlines()]


line_intersection = [value for value in Lines1 if value in Lines2]

line_intersection

#%%
# Dict Comprehension Challenge 1
"""
Instructions
You are going to use Dictionary Comprehension to create a dictionary 
called result that takes each word in the given sentence and calculates 
the number of letters in each word.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension 
instead of a Loop.
"""
sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'

split_sentence = sentence.split()

sentence_dict = {word : len(word) for word in split_sentence}

sentence_dict

# %%
# Challenge 2
"""
Instructions
You are going to use Dictionary Comprehension to create a dictionary 
called weather_f that takes each temperature in degrees Celsius and 
converts it into degrees Fahrenheit.

To convert temp_c into temp_f:
(temp_c * 9/5) + 32 = temp_f

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension 
instead of a Loop.
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {keys : (temp_c * 9/5) + 32 for keys, temp_c in weather_c.items()}

weather_f
# %%
