# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 11:51:35 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
from nltk.corpus import wordnet as wn

'''
Remove all non-nouns from the Bible and the Quran
'''


if __name__ == '__main__':

    '''
    All English nouns
    '''
    nouns = [str(x).split('.')[0].split("('")[1] for x in wn.all_synsets('n')]

    '''
    Data directory
    '''
    data_dir = '../Data/'

    '''
    Bible
    '''

    with open(data_dir + 'Bible.txt', 'r') as f_open:
        data = f_open.readlines()

    clean_bible = []

    for lines in data:
        clean_bible.append(" ".join(lines.replace('\t', ' ').split(' ')[2:]))

    clean_bible = " ".join(clean_bible)

    data = np.array(clean_bible.replace(';', '').
                    replace('\n', ' ').replace('.', '').
                    replace(',', '').replace(':', '').split(' '))

    print str(len(data)) + ' words in the Bible'

    '''
    Only nouns
    '''

    bible_nouns = []
    tot_words = len(data)

    tj = 0
    for i in data:
        tj += 1
        if not tj % 1000:
            print str(tj) + ' out of ' + str(tot_words)
        if i in nouns:
            bible_nouns.append(i)

    bible_nouns_arr = np.array(bible_nouns)

    print str(len(bible_nouns_arr)) + ' nouns in the Bible'

    np.savetxt(data_dir + 'Bible_nouns.txt', bible_nouns_arr, delimiter=" ", fmt="%s")

    '''
    Quran
    '''

    with open(data_dir + 'Quran.txt', 'r') as f_open:
        data = f_open.read()

    data = np.array(data.replace(';', '').
                    replace('\n', ' ').replace('.', '').
                    replace(',', '').replace(':', '').split(' '))

    print str(len(data)) + ' words in the Quran'

    '''
    Only nouns
    '''

    bible_nouns = []
    tot_words = len(data)

    tj = 0
    for i in data:
        tj += 1
        if not tj % 1000:
            print str(tj) + ' out of ' + str(tot_words)
        if i in nouns:
            bible_nouns.append(i)

    bible_nouns_arr = np.array(bible_nouns)

    print str(len(bible_nouns_arr)) + ' nouns in the Quran'

    np.savetxt(data_dir + 'Quran_nouns.txt', bible_nouns_arr, delimiter=" ", fmt="%s")
