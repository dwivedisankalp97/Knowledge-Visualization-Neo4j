from neo4jrestclient.client import GraphDatabase
import sys
db = GraphDatabase("http://localhost:7474", username="neo4j", password="sankalp")
excludewords = ["Breitbart News","The Wall street journal","BBC","The New York Times","The National Review","Breitbart","CBS","Donald Trump","CNN","Trump","CNBC","Reuters","Telegraph"]
excludewords2 = []
for x in excludewords:
    x = x.lower()
    excludewords2.append(x)
    
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
file_obj = open("finaldata1.csv","r",encoding="utf8")
finallist = []
for line in file_obj:
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    line = line.translate(non_bmp_map)
    line = line.translate({ord("'"):None})
    line = line.translate({ord('"'):None})
    line = line.translate({ord('“'):None})
    line = line.translate({ord('’'):None})
    #print("Line: ",line)
    templist = list(line.split(","))
    try:
        templist[0] = templist[0][1:]
        templist[0] = templist[0].strip()
        templist[1] = templist[1].strip()
        templist[2] = templist[2].strip()
        templist[3] = templist[3].strip()
        if templist[0].lower() in excludewords2 or templist[2].lower() in excludewords2:
            continue
    except IndexError:
        pass
    finallist.append(templist)
    print("Here:",templist)


for elem in finallist:
    if len(elem) != 4:
        continue
    if elem[0].isdigit() or elem[1].isdigit() or elem[2].isdigit():
        continue
    q = 'MERGE (u:entitity{name:"' + elem[0] +'"}) ' + 'MERGE (l:entitity{name:"' + elem[2] +'"}) ' + 'MERGE (u) -[:' + elem[1] + '{text: "'+ elem[3] +'"}] ->(l)'
    print(q)
    db.query(q)

