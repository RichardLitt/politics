import urllib2, sys, re, codecs
from BeautifulSoup import BeautifulSoup

# The name of the output file
output_file_name = 'obama_speeches' 
g = codecs.open(output_file_name, encoding='utf-8', mode='w+')
# A file with the PIDs of the pages, gotten by saving and regexing. 
# Should be made automatic, but lazy. 
input_file = 'presidency_pid' 
f = open(input_file, 'r+').readlines()

for numb in f:
    address = ('http://www.presidency.ucsb.edu/ws/index.php?pid=' + numb.strip())
    html = urllib2.urlopen(address).read()
    soup = BeautifulSoup(html)

    title = soup.find("span", {"class":"paperstitle"})
    date = soup.find("span", {"class":"docdate"})
    # span.string gives you the first bit
    span = soup.find("span", {"class":"displaytext"})  
    paras = [x for x in span.findAllNext("p")]

    first = title.string
    second = date.string

    # If you want to limit it to years. 
    #year = re.compile("\d\d\d\d")
    #match_o = re.search(year,second)
    #if int(match_o.group(0)) >= 2009: 

    start = span.string
    middle = "\n\n".join(["".join(x.findAll(text=True)) for x in paras[:-1]])

    # Some weird error. Not exactly necessary to keep everything.  
    try:
    	last = paras[-1].contents[0]
    except: continue

    file_name = 'speeches/' + str(first).strip().replace('\\','-').replace('/','-')[:100]

    h = codecs.open(file_name, encoding='utf=8', mode='w+')

    h.write("%s\n\n%s\n\n%s\n\n%s\n\n%s" % (first, second, start, middle, last))
    print 'Written: ' + str(first) #Just print the title so you can see what's going down. 
    h.close()
