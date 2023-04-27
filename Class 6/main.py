"""Find the average value of a specific key in a JSON file containing an array of dictionaries:
Write a Python program that reads a JSON file containing an array of dictionaries, calculates the average value of a
specific key across all dictionaries in the array, and prints the result. For example, given the following JSON file
named data.json"""

import json
# lines = ""
#
# with open("data.json", "r") as fhandle:
#     for line in fhandle:
#         lines += line
#
# new_file = json.loads(lines)
#
# nums = []
# for i in new_file:
#     nums.append(i["score"])
#
# print("Average Score:", sum(nums) / len(nums))

"""Write a Python program that reads a JSON file containing a list of numbers, finds the maximum and minimum values, 
and prints them to the console."""

lines = ""

with open("number.json", "r") as fhandle:
    for line in fhandle:
        lines += line

new_list = json.loads(lines)

print(max(new_list), min(new_list))