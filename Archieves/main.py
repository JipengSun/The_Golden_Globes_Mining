import json 
import pandas as pd
import re
import nltk
from nltk.util import ngrams
from collections import Counter
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer

data_path = "./gg2015.json"

collocation_words = {
    #"tv":"television",
    "pic":"picture",
    "for":"-",
    "in":"-",
    'or':'/',
    'of':'-'
}

skip_words = ['a']

paraphrase = [',','@','(',')','#']


def awards_mining(data_path):
    df = pd.read_json(data_path)
    strategy1 = common_phrases(keywords)
    votes = accumulate_votes(strategy1, strategy2, common_strings)




# Find a good format for award names.
def gram_cleaning(grams):
    new_grams = []
    for gram in grams:
        word_list = []
        for word in gram[0]:
            if word in collocation_words:
                word = collocation_words[word]
            if word in skip_words:
                break
            if word not in paraphrase:
                word_list.append(word)
        word_tuple = tuple(word_list)
        gram_tuple = (word_tuple,gram[1])
        new_grams.append(gram_tuple)
    return new_grams

# Separate 'A/B' type of words into 'A / B' to add more information to resolute.
def sticky_word_string(phrase):
    phrase_list = nltk.word_tokenize(phrase)
    token_list = []
    for word in phrase_list:
        flag = 0
        for i,character in enumerate(word):
            if character == '/' and i != 0:
                token_list.append(word[0:i])
                token_list.append(word[i])
                flag = i
                if i != len(word)-1:
                    token_list.append(word[i+1:len(word)])
                break
        if flag == 0 and word not in skip_words:
            token_list.append(word)
    clean_string = ' '.join(token_list)
    return clean_string

# Replacing some collocation words.
def string_cleaning(grams):
    new_grams = []
    for gram in grams:
        word_list = []
        clean_gram = sticky_word_string(gram[0])
        temp_list = nltk.word_tokenize(clean_gram)
        for word in temp_list:
            if word in collocation_words:
                word = collocation_words[word]
            if word not in paraphrase:
                word = word.strip()
                word_list.append(word)
        phrase = ' '.join(word_list)
        gram_tuple = (phrase,gram[1])
        new_grams.append(gram_tuple)
    return new_grams

'''
Input: gram sets
Output: phrases with frequency
'''
def accumulate_votes(grams1, grams2, common_strings):
    awards = {}
    '''
    for gram in grams1:
        untokenize = ' '.join(gram[0])
        awards[untokenize] = len(gram[0]) * gram[1]
    for gram in grams2:
        untokenize = ' '.join(gram[0])
        if untokenize in awards:
            awards[untokenize] = awards[untokenize] * 2.5
        else:
            awards[untokenize] = len(gram[0]) * gram[1]
    '''
    for string in common_strings:
        first_two = ' '.join(nltk.word_tokenize(string[0])[:2])
        if string[0] in awards:
            awards[string[0]] = awards[string[0]] * 2.5
        elif first_two in awards:
            awards[string[0]] = awards[first_two] * string[1]
        else:
            awards[string[0]] = len(string[0]) * string[1]
    return sorted(awards.items(), key = lambda x: x[1], reverse = True)
#Need a way to combine similar categories
print(len(votes))