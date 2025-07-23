# this code combines multiple dictionaries into one dictionary

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

d = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))

print("output:")
print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#method 2: Using ChainMap from collections
'''
from collections import ChainMap

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

d = dict(ChainMap(dic1, dic2, dic3))

print("output:")
print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

#method 3 : Using dictionary comprehension
'''
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

d = {**dic1, **dic2, **dic3} #展開dict

print("output:")
print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}   

'''

#method 4: Using update method
'''
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

d = dic()
d.update(dic1)
d.update(dic2)
d.update(dic3)

print("output:")
print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''


