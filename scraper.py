import urllib2,sys
import re
from BeautifulSoup import BeautifulSoup

output_file_name = 'obama_speeches' # The name of the output file
output = open(output_file_name,'w+') 


for numb in range(00001, 101999):
    address = ('http://www.presidency.ucsb.edu/ws/index.php?pid=' + str(numb))
    html = urllib2.urlopen(address).read()
    soup = BeautifulSoup(html)

    title = soup.find("span", {"class":"paperstitle"})
    date = soup.find("span", {"class":"docdate"})
    span = soup.find("span", {"class":"displaytext"})  # span.string gives you the first bit
    paras = [x for x in span.findAllNext("p")]

    first = title.string
    second = date.string
    year = re.compile("\d\d\d\d")
    match_o = re.search(year,second)
    if int(match_o.group(0)) >= 2009: 
	    start = span.string
	    middle = "\n\n".join(["".join(x.findAll(text=True)) for x in paras[:-1]])
	    try:
	    	last = paras[-1].contents[0]
	    except: continue

	    #print "%s\n\n%s\n\n%s\n\n%s\n\n%s" % (first, second, start, middle, last)
	    output.write("%s\n\n%s\n\n%s\n\n%s\n\n%s" % (first, second, start, middle, last))
	    print first
    #else: #print 'No match'
