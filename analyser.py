from __future__ import division
import urllib2, sys, re, codecs
import nltk, pprint
from BeautifulSoup import BeautifulSoup
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

# The name of the output file
#input_file_name = 'obama_speeches' 
#g = codecs.open(input_file_name, mode='r+').read()

#g = nltk.Text(nltk.word_tokenize(g))
#print g.concordance('freedom')
#print g.concordance('liberty')

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/richard/Github/politics/speeches/'
ocorpus = PlaintextCorpusReader(corpus_root, '.*')
for fileid in ocorpus.fileids():
	num_chars = len(ocorpus.raw(fileid))
	num_words = len(ocorpus.words(fileid))
	num_sents = len(ocorpus.sents(fileid))
	num_vocab = len(set([w.lower() for w in ocorpus.words(fileid)]))
	#print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid
	print nltk.Text(ocorpus.words(fileid)).concordance('freedom')
	print nltk.Text(ocorpus.words(fileid)).concordance('liberty')