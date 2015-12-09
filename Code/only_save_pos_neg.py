# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 11:51:35 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np


'''
Create positive and negative versions of the Bible and the Quran
'''


if __name__ == '__main__':

    '''
    Data directory
    '''
    data_dir = '../Data/'

    '''
    Load positive and negative lists
    '''
    neg_comp = np.genfromtxt(data_dir + 'negative_words.txt', delimiter='\n', dtype=np.str, autostrip=True)
    pos_comp = np.genfromtxt(data_dir + 'positive_words.txt', delimiter='\n', dtype=np.str, autostrip=True)

    '''
    Positive and negative nouns
    '''

    txts = ['Bible', 'Quran']
    for j in txts:
        data = np.genfromtxt(data_dir + j + '_nouns.txt', delimiter='\n', dtype=np.str, autostrip=True)

        '''
        Sorting
        '''

        bible_neg = []
        bible_pos = []
        tot_words = len(data)

        tj = 0
        for i in data:
            tj += 1
            if not tj % 10000:
                print str(tj) + ' out of ' + str(tot_words)
            if i in pos_comp:
                bible_pos.append(i)
            elif i in neg_comp:
                bible_neg.append(i)

        bible_neg_arr = np.array(bible_neg)
        bible_pos_arr = np.array(bible_pos)

        print str(len(bible_neg_arr)) + ' negative words in the ' + j
        print str(len(bible_pos_arr)) + ' positive words in the ' + j

        np.savetxt(data_dir + j + '_neg.txt', bible_neg_arr, delimiter=" ", fmt="%s")
        np.savetxt(data_dir+ j + '_pos.txt', bible_pos_arr, delimiter=" ", fmt="%s")
