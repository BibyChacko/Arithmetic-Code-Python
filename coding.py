# Program for generating Aritmetic code of any string given its symbols
#     and probabilities of occurence

def binaryEncoding(lb,ub,taglb,tagub,val):
    mid = (lb+ub)/2
    if((taglb <= lb) and  (tagub >= ub)):
        print("code = "+val)              # Printing the output code
        exit()
    else:
        if((taglb > mid) and (tagub <ub)): # Comparison for the lower - bound
            binaryEncoding(mid,ub,taglb,tagub,val+"1")

        elif ((tagub > mid) and (taglb < lb)  ):    #Comparison for the upper - bound
            binaryEncoding(lb, mid, taglb, tagub, val + "0")

        elif((taglb > lb) and (tagub > mid)):        #Comparison for the upper - bound
            binaryEncoding(mid, ub, taglb, tagub, val + "1")


        else:
            binaryEncoding(lb,mid,taglb,tagub,val+"0")

def findSymbol(lb,ub,index):
    if (index == len(ipString)):
        print("Interval =[" + str(lb) + "," + str(ub) + "]")        # Printing the Interval
        taglb = lb
        tagub = ub
        binaryEncoding(0, 1,taglb,tagub, "")                        # function call for encoding the interval

    dataSymbol = ipString[index]
    lenRange =ub-lb

    for sym in table:
        if(sym==dataSymbol):
             findSymbol(lb,lb+(table.get(sym)*lenRange),index+1)
        else:
            lb = lb+(table.get(sym) *lenRange)



symbols = input("Enter the symbols")
symbols =symbols.split(" ")
table = {}
ipString = ""
for i in symbols:
    x = float(input("enter the probabilty of "+ i))
    table.setdefault(i,x)

if(sum(table.values())!=1):
    print("invalid probability")

else:
    ipString = input("Enter the string")
    findSymbol(0,1,0)

