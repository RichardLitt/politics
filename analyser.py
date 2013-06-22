from __future__ import division
import urllib2, sys, re, codecs, nltk, pprint
from BeautifulSoup import BeautifulSoup
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

# The name of the output file
input_file_name = 'obama_speeches' 
g = codecs.open(input_file_name, mode='r+').read()

g = nltk.Text(nltk.word_tokenize(g))
print g.concordance('freedom')
print g.concordance('liberty')