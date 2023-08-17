## https://adventofcode.com/2021/day/5


## See if you can take advantage of python regex to read in the input data.  I think in this case it works better than for some of the other day's data.
## 
import re
##m = re.search(r'(?<=-)\w+', 'spam-egg')
##m.group(0)
##print (m.group(0))

## open the file containing the list of lines
inputfile = open("linesin.txt","r")
lines = inputfile.readlines()

for line in lines:
    #print(line, end="")
    start, stop = re.split(" -> ", line) ## first split apart the start and stop values seperated by ->
    startx, starty = re.split(",", start) ## then split the x and y values seperated by a ,
    stopx, stopy = re.split(",", stop) 
    print (start, stop)
    test = int(startx) ## this works but cant get map to work
    test2 = list(map(int,startx))
    
    print (test2)
##    print (test2+1)
    print (startx, starty, "stop ", stopx, stopy, int(stopx)+1)