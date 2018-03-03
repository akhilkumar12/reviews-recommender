# -*- coding: cp1252 -*-
## Finds the opinion word

from pycorenlp import StanfordCoreNLP
from PyDictionary import PyDictionary
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
nlp = StanfordCoreNLP('http://localhost:9000')

##text = (
##  'But if you want to reduce the volume before playing the media, let us say because you do not want to start playing too loudly, then you cannot use the volume rocker, because it would only change the ring volume at that time.')
##
##output = nlp.annotate(text, properties={
##  'annotators': 'tokenize,ssplit,pos,depparse,parse',
##  'outputFormat': 'json'
##  })
##
##print output
##print output['sentences']
##print "\nasdasdas\n"
##print output['sentences'][0]
##
##for i in (output['sentences'][0]):
##    print i
##    print output['sentences'][0][i]
##    print("Some Random Text to differentiate\n\n")
##
##feature = "time"
##opinion_word = ""
##
##for i in range(len(output['sentences'][0]['basic-dependencies'])):
##    print output['sentences'][0]['basic-dependencies'][i]
##    print output['sentences'][0]['basic-dependencies'][i]['dep']
##    print("\n\n")
##    if output['sentences'][0]['basic-dependencies'][i]['dep'] == "amod" and output['sentences'][0]['basic-dependencies'][i]['governorGloss'] == feature:
##        opinion_word = output['sentences'][0]['basic-dependencies'][i]['dependentGloss']
##    elif output['sentences'][0]['basic-dependencies'][i]['dep']=="nsubj" and output['sentences'][0]['basic-dependencies'][i]['dependentGloss'] == feature and output['sentences'][0]['basic-dependencies'][i+1]['dep']=="advmod":
##        opinion_word = output['sentences'][0]['basic-dependencies'][i+1]['dependentGloss']
##    elif output['sentences'][0]['basic-dependencies'][i]['dep']=="nsubj" and output['sentences'][0]['basic-dependencies'][i]['dependentGloss'] == feature:
##        opinion_word = output['sentences'][0]['basic-dependencies'][i]['governorGloss']
##
##print opinion_word


input_list = []

fo = open("final_features1.txt", "r+")
input_string = fo.read()

output_string = input_string.split("~")
print(output_string)

feature_list = []
temp=[]
for i in output_string:
    input_list.append(i)
for i in input_list:
    temp=i.split(" ")
    feature_list.append(temp)
print "Feature List"
for i in feature_list:
    for j in i:
        print j
    

review_list = []
fo = open("p2 1+2.txt", "r+")
review_input = fo.read()

review_output = review_input.split("~")

for i in review_output:
    review_list.append(i)

for i in review_list:
    print i

one_review = []
sent = []
for i in review_list:
    sent = i.split(".")
    one_review.append(sent)

print "One Review"
for i in one_review:
    print i

print "\nMain code\n"

final_output = []
temp1 = []

for i in range(len(one_review)):
    for j in one_review[i]:
        temp = j.split(" ")
        for k in feature_list[i]:
            if k in temp and len(k)>2 and len(j)>2:
                text = j
                output = nlp.annotate(text, properties={
                  'annotators': 'tokenize,ssplit,pos,depparse,parse',
                  'outputFormat': 'json'
                  })
                feature = k
                opinion_word = "test"
                print "text:", text, ":text"
                print "feature:", feature, ":feature"
                for ind in range(len(((output['sentences'])[0])['basic-dependencies'])):
                    print output['sentences'][0]['basic-dependencies'][ind]
                    print output['sentences'][0]['basic-dependencies'][ind]['dep']
                    print("\n\n")
                    if output['sentences'][0]['basic-dependencies'][ind]['dep'] == "amod" and output['sentences'][0]['basic-dependencies'][ind]['governorGloss'] == feature:
                        opinion_word = output['sentences'][0]['basic-dependencies'][ind]['dependentGloss']
                    elif (ind+1)!=len((output['sentences'][0]['basic-dependencies'])):
                        if output['sentences'][0]['basic-dependencies'][ind]['dep']=="nsubj" and output['sentences'][0]['basic-dependencies'][ind]['dependentGloss'] == feature and output['sentences'][0]['basic-dependencies'][ind+1]['dep']=="advmod":
                            opinion_word = output['sentences'][0]['basic-dependencies'][ind+1]['dependentGloss']
                    elif output['sentences'][0]['basic-dependencies'][ind]['dep']=="nsubj" and output['sentences'][0]['basic-dependencies'][ind]['dependentGloss'] == feature:
                            opinion_word = output['sentences'][0]['basic-dependencies'][ind]['governorGloss']

                print "text: ", text
                print "feature: ", feature
                print "opinion word", opinion_word
                if opinion_word!="test":
                    temp1.append((feature,opinion_word))
                    print "temp1 ", temp1
    final_output.append(temp1[:])
    del temp1[:]

for i in final_output:
    print i

print "Feature vs opinion Word ", final_output

file = open("feature_opinion.txt", "w")

for i in final_output:
    for j in i:
        file.write("%s:%s " %(j[0], j[1]))
    file.write("~")

file.close()



# Finding orientation of the opinion word

def orientation(word):
    print "\nWord= ", word
    test2 = word
    score = None
    try:
        tmp = wn.synsets(test2)[0].pos()
        test1 = test2+"."+tmp+".01"
        score = swn.senti_synset(test1)
        print "score", score
        if (score.pos_score() - score.neg_score())!=0:
            return (score.pos_score() - score.neg_score())
    except:
        print "Exception"
##    print(score)

    if score==None or score.pos_score() - score.neg_score()==0.0:
        synonyms = []
        antonyms = []

        dictionary=PyDictionary()
        
        synonyms=dictionary.synonym(test2)
        print synonyms
        final_score = 0
        count = 0
        if synonyms!=None:
            for i in synonyms:
                print(i)
                try:
                    tmp = wn.synsets(i)[0].pos()
                    j = i+"."+tmp+".01"
                    score = swn.senti_synset(j)
                except:
                    print "Exception"
                
                print(score)
                if score!=None and (score.pos_score()-score.neg_score()) != 0:
                    final_score = final_score + (score.pos_score()-score.neg_score())
                    count = count+1
                print "final score ", final_score
            try:
                if count!=0:
                    final_score = final_score/count
            except:
                print "Exception Zero Division Error"
            print final_score
        
        
        antonyms=dictionary.antonym(test2)
        print(antonyms)
        final_score2 = 0
        count2 = 0
        if antonyms!=None:
            for i in antonyms:
                print(i)
                try:
                    tmp = wn.synsets(i)[0].pos()
                    j = i+"."+tmp+".01"
                    score = swn.senti_synset(j)
                except:
                    print "Exception"
                
                print(score)
                if score!=None and (score.pos_score()-score.neg_score()) !=0:
                    final_score2 = final_score2 + (score.pos_score()-score.neg_score())
                    count2 = count2+1
                print "final score2 ", final_score2
            try:
                if count!=0:
                    final_score2 = final_score2/count2
            except:
                print "Exception Zero Division Error"
            print final_score2


    if final_score!=None or final_score!=0:
        return final_score
    elif final_score2!=None or final_score2!=0:
        return (-1*final_score2)
    else:
        return 0




opinion_dict = {}
count_dict = {}
tempscore = 0
for i in final_output:
    for j in i:
        if opinion_dict.has_key(j[0]):
            opinion_dict[j[0]]+= orientation(j[1])
            count_dict[j[0]]+=1
        else:
            opinion_dict[j[0]]= orientation(j[1])
            count_dict[j[0]]=1


print "opinion Dictionary ", opinion_dict
print "Count Dictionary ", count_dict
for i,j in opinion_dict.items():
    print i, ":", j

for k in opinion_dict.keys():
    opinion_dict[k] = opinion_dict[k]/count_dict[k]
    print opinion_dict[k]

print "opinion Dictionary ", opinion_dict
for i,j in opinion_dict.items():
    print i, ":", j





                                           
