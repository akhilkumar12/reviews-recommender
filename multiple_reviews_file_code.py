## This code reads data from a file and
## splits it about a certain character.

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize, sent_tokenize


input_list = []


fo = open("p1 one plus x.txt", "r+")
input_string = fo.read()

output_string = input_string.split("~")

for i in output_string:
    input_list.append(i)

##print(input_list)

#list to store frequent words
frequent_words = []
tokenized = []
for i in range(0,len(input_list)):  ## number of reviews in a single file.
    sent = sent_tokenize(input_list[i])
    tokenized.append(sent)

for i in tokenized:
    print(i)

def process_content():
    try:
        for i in tokenized:
            random = []
            for j in i:
                words = nltk.word_tokenize(j)
                tagged = nltk.pos_tag(words)
                for k in tagged:
                    print(k)
                    if k[1]=="NN" :
                        random.append(k[0])
            frequent_words.append(random)
                        

    except Exception as e:
        print(str(e))

process_content()

file = open("initial_features1.txt", "w")

for i in range(len(frequent_words)):
    for j in range(len(frequent_words[i])):
        if j<len(frequent_words[i])-1:
           file.write("%s " %frequent_words[i][j])
        else:
            file.write("%s" %frequent_words[i][j])
        print(frequent_words[i][j])
    file.write("~")
    print("\n")
    
file.close()

print "\n\n"
for i in range(len(frequent_words)):
    print "Review ", i, " "
    print frequent_words[i]
