## This code reads reviews from a file and fetches
## nouns and then apply APRIORI ALGO to them.

from collections import defaultdict
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize, sent_tokenize
import shlex

fo = open("initial_features1.txt", "r+")
input_string = fo.read()

my_splitter = shlex.shlex(input_string, posix=True)
my_splitter.whitespace += '~'
my_splitter.whitespace_split = True
print list(my_splitter)

print(shlex.split(input_string, "~"))

output_string = input_string.split("~")
print(input_string)
print("\n")
print(output_string)
print("\n")

frequent_words = []

for i in output_string:
    output2 = i.split(" ")
    frequent_words.append(output2)

for i in frequent_words:
    for j in i:
        print j
    print("\n")


##frequent_words = [['l1', 'l2', 'l5'],['l2', 'l4'],['l2', 'l3'],['l1', 'l2', 'l4'],['l1', 'l3'],['l2', 'l3'],['l1', 'l3'],['l1', 'l2', 'l3', 'l5'],['l1', 'l2', 'l3']]
##print(frequent_words)

min_sup = 1
min_conf = 0.4

hash_map = {}
final_map = {}
itemset_1 = defaultdict(list)
rows = len(frequent_words)
cols = len(frequent_words[0])

# Generating 1 itemset frequent pattern
for i in range(rows):
    print ("Value of i= "), i
    for j in range(len(frequent_words[i])):
        if hash_map.has_key(frequent_words[i][j]):
            hash_map[frequent_words[i][j]]=hash_map[frequent_words[i][j]]+1
            itemset_1[frequent_words[i][j]].append(i)
##            print ("Old entry"), (itemset_1)
        else:
            hash_map[frequent_words[i][j]]=1
            itemset_1[frequent_words[i][j]].append(i)
##            print("new entry"), (itemset_1)


print("Initial Hashmap")
for i in hash_map:
    print(i)
    print(hash_map[i])
    if hash_map[i] >= min_sup:
        final_map[i] = hash_map[i]

print("\n\nFinal Hashmap")
for i in final_map:
    print(i)
    print(final_map[i])

print("\n\nItemSet")
print(itemset_1)
for i in itemset_1:
    print i
    print("\n")
    


# Generating 2 itemset frequent pattern

# Function for finding common reviews for 2 features
def merge_itemset1(list_1, list_2):
    store_list=[]
    ind1=0
    ind2=0
    while ind1<len(list_1) and ind2<len(list_2):
        if list_1[ind1]==list_2[ind2]:
            store_list.append(list_1[ind1])
            ind1+=1
            ind2+=1
        elif list_1[ind1]<list_2[ind2]:
            ind1+=1
        else:
            ind2+=1
    
    return store_list


itemset_2 = []
final_itemset2 = []
review_no2 = []
final_reviewNo2 = []
size = (len(final_map)*(len(final_map)-1))/2
##print(size)

#for i in range(size):
    #itemset_2.append([])

for i in range(len(final_map)):
    for j in range(i+1,len(final_map)):
        if i!=j:
            itemset_2.append((list(final_map)[i], list(final_map)[j]))

print("ITEMSET2")
print(itemset_2)

print("Something Something")
for i in range(len(itemset_2)):
    list_1 = itemset_1[itemset_2[i][0]]
    list_2 = itemset_1[itemset_2[i][1]]
    print(list_1)
    print(list_2)
    review_no2.append(merge_itemset1(list_1, list_2))

print("Review No2")
print(review_no2)

print("InitialSize: "), len(review_no2)

for i in range(len(itemset_2)):
    if len(review_no2[i])>=2:
       final_itemset2.append((itemset_2[i][0], itemset_2[i][1]))
       final_reviewNo2.append(review_no2[i])

print("FinalSize: "), len(final_itemset2)
print(final_itemset2)
print(final_reviewNo2)



# Generating 3 itemset frequent pattern

def merge_itemset2(l1,l2,l3):
    store_list = []
    i=0
    j=0
    k=0
    while i<len(l1) and j<len(l2) and k<len(l3):
        if l1[i]==l2[j] and l1[i]==l3[k]:
            store_list.append(l1[i])
            i+=1
            j+=1
            k+=1
        else:
            minm = min(l1[i],l2[j],l3[k])
            if minm==l1[i]:
                i+=1;
            if minm==l2[j]:
                j+=1;
            if minm==l3[k]:
                k+=1;

    return store_list

itemset_3 = []
review_no3 = []
final_itemset3 = []
final_reviewNo3 = []

print ("Final itemset2 "), final_itemset2

new_map = []

for i in final_itemset2:
    if i[0] not in new_map:
        new_map.append(i[0])
    if i[1] not in new_map:
        new_map.append(i[1])

print ("New_map"), new_map

mat_size = len(new_map)
intermediate_matrix = [[0 for x in range(mat_size)] for x in range(mat_size)]

for i in final_itemset2:
    string1 = i[0]
    string2 = i[1]
    print string1
    print string2
    print new_map.index(i[0])
    print new_map.index(i[1])
    intermediate_matrix[new_map.index(i[0])][new_map.index(i[1])] = 1

print(intermediate_matrix)

print("mat size: "), mat_size

for i in range(mat_size):
    for j in range(mat_size):
        if intermediate_matrix[i][j]==1:
            for k in range(j+1, mat_size):
                if intermediate_matrix[i][k]==1:
                    if intermediate_matrix[j][k]==1 or intermediate_matrix[k][j]==1:
                        itemset_3.append((new_map[i],new_map[j],new_map[k]))

print(itemset_3)
print "size: ", len(itemset_3)

for i in itemset_3:
    if (i[0],i[1]) in final_itemset2:
        l1 = final_reviewNo2[final_itemset2.index((i[0],i[1]))]
    else:
        l1 = final_reviewNo2[final_itemset2.index((i[1],i[0]))]
    if (i[0],i[2]) in final_itemset2:
        l2 = final_reviewNo2[final_itemset2.index((i[0],i[2]))]
    else:
        l2 = final_reviewNo2[final_itemset2.index((i[2],i[0]))]
    if (i[1],i[2]) in final_itemset2:
        l3 = final_reviewNo2[final_itemset2.index((i[1],i[2]))]
    else:
        l3 = final_reviewNo2[final_itemset2.index((i[2],i[1]))]
    review_no3.append(merge_itemset2(l1,l2,l3))

print "review_no3"
print(review_no3)

for i in range(len(itemset_3)):
    if len(review_no3[i])>=2:
       final_itemset3.append((itemset_3[i][0], itemset_3[i][1], itemset_3[i][2]))
       final_reviewNo3.append(review_no3[i])

print(final_itemset3)
##print(final_reviewNo3)
    
new_map2 = []

for i in final_itemset3:
    if i[0] not in new_map2:
        new_map2.append(i[0])
    if i[1] not in new_map2:
        new_map2.append(i[1])
    if i[2] not in new_map2:
        new_map2.append(i[2])

print ("New_map2"), new_map2

new_list = []
final_features = []

for i in frequent_words:
    for j in new_map2:
        print "i= ", i
        print "j= ", j
        if j in i:
            new_list.append(j)
        print "new list ", new_list
    final_features.append(new_list[:])
    print "final= ", final_features
    del new_list[:]

for i in final_features:
    print i

file = open("final_features1.txt", "w")
for i in final_features:
    for j in i:
        file.write("%s " %j)
    file.write("~")

file.close()

print"\n"
for i in range(len(final_features)):
    print "Review ", i, " "
    print final_features[i]







        

