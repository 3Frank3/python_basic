
# string_replaced.py
# This code replaces the phrase "not … at all" with "good" in a given string.

print("type your input :")
s = input()  # This company is not poor at all.

s1 = s.split("not ")[0] # This company is

s2 = s.split("at all")[1] 

d = f"{s1}good{s2}"

print("output:")
print(d) #This company is good.


#method 2
'''
f1 = s.find("not ")

f2 = s.find("at all")+6

d = s[:f1] + "good" + s[f2:]
'''
