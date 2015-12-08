# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 22:21:14 2015

@author: Marcus Therkildsen
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

'''
Bible: http://www.truth.info/download/bible.htm
Quran: https://archive.org/stream/TheQuranKoranenglishEbook-AbdelHaleem-BestTr
anslationInThe/the_QURAN-abdel-haleem-ebook-english_djvu.txt

Positive words: https://github.com/williamgunn/SciSentiment/blob/master/positive-words.txt
Negative words: https://github.com/williamgunn/SciSentiment/blob/master/negative-words.txt
'''

# Change mathtext to follow text regular size
plt.rcParams['mathtext.default'] = 'regular'

# Change all fonts to certain size unless otherwise stated
font = {'size': 14}
plt.rc('font', **font)

if __name__ == '__main__':

    '''
    Counting
    '''

    # How many to print
    top = 10

    # Load the bible and quran
    txts = ['Bible', 'Quran']
    plus = '_nouns'

    top_words_name = np.chararray([len(txts), top], itemsize=50)
    top_words_count = np.empty([len(txts), top], dtype=np.single)

    tot_nouns = np.empty(2)
    tj = -1
    for j in txts:
        tj += 1
        frequencies = Counter()
        with open(j + plus + '.txt') as f:
            for line in f:
                frequencies.update(line.lower().split())

        tot_words = np.sum(frequencies.values(), dtype=np.single)

        tot_nouns[tj] = tot_words

        print 'Total words in the ' + j + ': ' + str(int(tot_words))

        most_frequent = np.array(sorted(frequencies.most_common(top),
                                 key=lambda (x, y): (y, x)))

        top_words_name[tj, :] = most_frequent[:, 0]
        top_words_count[tj, :] = most_frequent[:, 1].astype(
                                 np.single)/tot_words

    '''
    PLOT
    '''

    c_all = ['#197319', '#2F2FC0']

    for i in xrange(2):
        fig, ax = plt.subplots()
        ax.grid()
        ax.barh(np.arange(top)+0.5, top_words_count[i, :], 1, color=c_all[i], zorder = 100)
        ax.set_ylim(0, top+1)
        ax.set_xlim(np.min(top_words_count[i, :])*0.9,
                    np.max(top_words_count[i, :])*1.1)
        ax.set_yticks(np.arange(top)+1)
        ax.set_yticklabels(top_words_name[i, :])

        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.locator_params(axis='x', nbins=6)

        ax.set_xlabel('%')
        if len(plus) is 0:
            to_title = txts[i]
            to_save = txts[i]
        else:
            to_title = txts[i] + ' nouns'
            to_save = txts[i] + '_nouns'

        ax.set_title(to_title)
        plt.tight_layout()
        plt.savefig(to_save + '.png', dpi=400)

        plt.show()


###############################################################################

    # Load the bible and quran
    top = 10
    txts = ['Bible', 'Quran']
    perc_ = np.empty([2, 2])
    kj = -1
    for temp in ['neg', 'pos']:
        kj += 1
        plus = '_'+temp

        top_words_name = np.chararray([len(txts), top], itemsize=50)
        top_words_count = np.empty([len(txts), top], dtype=np.single)

        tj = -1
        for j in txts:
            tj += 1
            frequencies = Counter()
            with open(j + plus + '.txt') as f:
                for line in f:
                    frequencies.update(line.lower().split())

            tot_words = np.sum(frequencies.values(), dtype=np.single)

            # print 'Total words in the ' + j + ': ' + str(int(tot_words))

            perc_[kj, tj] = 100*tot_words/tot_nouns[tj]

            most_frequent = np.array(sorted(frequencies.most_common(top),
                                     key=lambda (x, y): (y, x)))

            top_words_name[tj, :] = most_frequent[:, 0]
            top_words_count[tj, :] = most_frequent[:, 1].astype(
                                     np.single)/tot_words

        '''
        PLOT
        '''

        for i in xrange(2):
            fig, ax = plt.subplots()
            ax.grid()
            ax.barh(np.arange(top)+0.5, top_words_count[i, :], 1, color=c_all[i], zorder = 100)
            ax.set_ylim(0, top+1)
            ax.set_xlim(np.min(top_words_count[i, :])*0.9,
                        np.max(top_words_count[i, :])*1.1)
            ax.set_yticks(np.arange(top)+1)
            ax.set_yticklabels(top_words_name[i, :])

            ax.xaxis.set_ticks_position('none')
            ax.yaxis.set_ticks_position('none')
            ax.locator_params(axis='x', nbins=6)

            ax.set_xlabel('%')
            if len(plus) is 0:
                to_title = txts[i]
                to_save = txts[i]
            else:
                to_title = txts[i] + ' ' + temp
                to_save = txts[i] + plus

            ax.set_title(to_title)
            plt.tight_layout()
            plt.savefig(to_save + '.png', dpi=400)

            plt.show()

    '''
    Pos/neg ratio
    '''
    # perc_: (neg/pos, bible/quran)
    for_pie = [(perc_[1, 0]/perc_[0, 0]), (perc_[1, 1]/perc_[0, 1])]

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Bible', 'Quran'
    sizes = for_pie

    plt.pie(sizes, labels=labels, colors=c_all,
            autopct='%1.1f%%', shadow=False, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('Pos/neg ratio')
    plt.savefig('pos_neg_ratio.png', dpi=400)
    plt.show()

    '''
    Kill, famine, pain, death(+dead)
    '''
    bad_words = np.array(['kill', 'famine', 'pain', 'death', 'dead'])
    top = len(bad_words)
    top_words_count = np.zeros([len(txts), top])
    top_words_name = np.chararray([len(txts), top], itemsize=50)

    # Bible, Quran
    for k in xrange(len(txts)):
        bad_words_num = np.zeros(top)

        data = np.genfromtxt(txts[k] + '_neg.txt', delimiter='\n', dtype=np.str, autostrip=True)

        for i in xrange(len(data)):
            if data[i] in bad_words:
                for jk in xrange(top):
                    if data[i] == bad_words[jk]:
                        bad_words_num[jk] += 1
        #print bad_words
        #print bad_words_num
        da_num = 100*bad_words_num/tot_nouns[k]
        da_num_ind = np.argsort(da_num)

        top_words_count[k, :] = 100*bad_words_num[da_num_ind]/tot_nouns[k]
        top_words_name[k, :] = bad_words[da_num_ind]


    '''
    K/D score
    '''
    rev_top_words_count = top_words_count[:, ::-1]
    rev_top_words_name = top_words_name[:, ::-1]


    k_d = np.zeros(len(txts))
    for k in xrange(len(txts)):

        k_d[k] = rev_top_words_count[k, 2] / (rev_top_words_count[k, 0] + rev_top_words_count[k, 1])



    '''
    PLOT
    '''

    for k in xrange(len(txts)):
        fig, ax = plt.subplots()
        ax.grid()
        ax.barh(np.arange(top)+0.5, top_words_count[k, :], 1, color=c_all[k], zorder = 100)
        ax.set_ylim(0, top+1)
        ax.set_xlim(np.min(top_words_count[k, :])*0.9,
                    np.max(top_words_count[k, :])*1.1)
        ax.set_yticks(np.arange(top)+1)
        ax.set_yticklabels(top_words_name[k, :])

        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.locator_params(axis='x', nbins=6)

        ax.set_xlabel('%')
        ax.set_title(txts[k])
        plt.tight_layout()
        plt.savefig(txts[k] + '_bad_words.png', dpi=400)

        plt.show()

    '''
    K/D ratio bar chart
    '''
    top = 2
    fig, ax = plt.subplots()
    ax.grid()
    ax.bar(np.arange(top)+0.5, k_d, 1, color=c_all, zorder=100)
    ax.set_xlim(0, top+1)
    ax.set_ylim(0, np.max(k_d)*1.1)
    ax.set_xticks(np.arange(top)+1)
    ax.set_xticklabels(txts)

    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.locator_params(axis='y', nbins=6)

    ax.set_title('K/D ratio')
    plt.tight_layout()
    plt.savefig('k_d_ratio.png', dpi=400)
    plt.show()
