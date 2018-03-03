## This code stores a 2d list of features vs products
## and recommends products based on those features.

from random import randint
import random
import json

p1 = {'phone': 0.15300000000000002, 'use': 0, 'camera': -0.16666666666666666, 'quality': -0.08333333333333333}
p2 = {'issue': 0.125, 'phone': 0.125, 'camera': 0, 'time': 0, 'usage': 0.05555555555555555, 'performance': 0.3125, 'quality': 0.625, 'day': 0.0, 'software': 0.375}
p3 = {'life': 0.5, 'management': -0.125, 'scanner': 0, 'battery': 0.125, 'use': 0, 'phone': 0.25, 'camera': 0.5, 'performance': 0.4375, 'bit': -0.25, 'quality': 0.3125, 'display': 0.125}
p4 = {'product': 0, 'issue': 0.125, 'look': 0.125, 'phone': -0.375, 'battery': 0.125, 'light': -0.0625, 'price': -0.25, 'apps': 0.125, 'sale': 0, 'glass': 0.16666666666666666, 'response': 0, 'thing': 0.4583333333333333, 'Battery': 0, 'camera': -0.14583333333333334, 'video': -0.25, 'mobile': 0, 'time': -0.02777777777777778, 'device': 0.0, 'design': 0.1875, 'quality': 0.22916666666666666, 'screen': 0.125}
p5 = {'battery': -0.5, 'moto': 0, 'phone': 0.59375, 'camera': 0.5, 'usage': 0.25, 'day': -0.0625}


# save to file:
with open('my_file1.json', 'w') as f1:
    json.dump(p1, f1)
with open('my_file2.json', 'w') as f2:
    json.dump(p2, f2)
with open('my_file3.json', 'w') as f3:
    json.dump(p3, f3)
with open('my_file4.json', 'w') as f4:
    json.dump(p4, f4)
with open('my_file5.json', 'w') as f5:
    json.dump(p5, f5)

data = {}
# load from file:
with open('my_file1.json', 'r') as f:
    try:
        temp = json.load(f)
    # if the file is empty the ValueError will be thrown
    except ValueError:
        temp = {}
data['r1']=temp

# load from file:
with open('my_file2.json', 'r') as f:
    try:
        temp = json.load(f)
    # if the file is empty the ValueError will be thrown
    except ValueError:
        temp = {}
data['r2']=temp

# load from file:
with open('my_file3.json', 'r') as f:
    try:
        temp = json.load(f)
    # if the file is empty the ValueError will be thrown
    except ValueError:
        temp = {}
data['r3']=temp

# load from file:
with open('my_file4.json', 'r') as f:
    try:
        temp = json.load(f)
    # if the file is empty the ValueError will be thrown
    except ValueError:
        temp = {}
data['r4']=temp

# load from file:
with open('my_file5.json', 'r') as f:
    try:
        temp = json.load(f)
    # if the file is empty the ValueError will be thrown
    except ValueError:
        temp = {}
data['r5']=temp


print "Data\n"
for i,j in data.items():
    print i,j
print "\nData"  

temp_dict = {}

for i in data.values():
    for j in i.keys():
        if not temp_dict.has_key(j):
            temp_dict[j]=1

print temp_dict        

w,h=5,len(temp_dict)
Matrix = [[0 for x in range(h)] for y in range(w)]
print Matrix
temp_list = []
for i in temp_dict.keys():
    temp_list.append(i)

print temp_list
print len(temp_list)
print w,h

for i in range(w):
    for j in range(h):
        ind = "r"+str(i+1)
        if data[ind].has_key(temp_list[j]):
            Matrix[i][j] = data[ind][temp_list[j]]
        else:
            Matrix[i][j]=0

print "\nMatrix"
for i in Matrix:
    print i

print "\nHere is the list of features"
for i in range(len(temp_list)):
    print i, ":", temp_list[i]

print "\nChoose your top 5 preferences"

string_input = raw_input()
input_list = string_input.split() #splits the input string on spaces
# process string elements in the list and make them integers
input_list = [int(a) for a in input_list] 

##print input_list
final_score = []
score=0
for i in range(w):
    for j in range(len(input_list)):
        score += Matrix[i][input_list[j]]*(5-j)*(5-j)
##        print "Score: ", score
    final_score.append(score)
    score=0
##    print "\n"

print "Final score of each product"
print final_score
phone = ['one plus x','one plus two','redmi note3','k3 note','motog4']
print "\nRecommended phone is: ", phone[final_score.index(max(final_score))]
