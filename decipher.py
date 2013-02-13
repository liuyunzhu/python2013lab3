# decipher.py
# author: Liu Yunzhu
# to decipher encrypted input file and output top 3 words on output file

infile = open("MYSTERY.IN",'r')
outfile = open("RESULT.OUT",'w')

try:
    lines = infile.readlines()

    chrlist =[]
    for line in lines:
        for n in range (0, len(line)):
            chrlist.append(line[n])
    combined = ''
    for chrs in chrlist:
       # print(chr(ord(chrs) - 5), end="")
        combined = combined + chr(ord(chrs) - 5)

# find the top 3 words
    words =[]
    occurence ={}
    combined = combined.lower()
    words.append(combined.split())
    words = words[0]

    #count occurence
    for word in words:
        for a in range(0,len(words)):
            occurence = {words[a]:words.count(words[a])}
            
            print (occurence)

    infile.close()
    outfile.close()

except IOError:
    print("cannot read from MYSTERY.IN or cannot output to RESULT.OUT")
