
import spacy
from textpipeliner import PipelineEngine, Context
from textpipeliner.pipes import *
from spacy import displacy
import glob
import errno

finallist = []
def list_create(a,line,finallist):
    templist = []
    for x in a[0][1]:
        x = str(x)
        z = nlp(x)
        for token in z:
            le = token.lemma_;
            break
        #print(le)
        if le in keywords_nlp:
            print("Relationship Match")
            templist = []
            temps=""
            tempss=""
            for y in a[0][0]:
                y = str(y)
                temps = "".join(y)
                tempss = tempss + " " + temps
            templist.append(tempss)
            templist.append(le)
            temps=""
            tempss=""
            for y in a[0][2]:
                y = str(y)
                temps = "".join(y)
                tempss = tempss + " " + temps
            templist.append(tempss)
            templist.append(line)
            #print("here",templist)
            break
    if(templist):
        if templist[0] != templist[2]:
            print(templist)
            finallist.append(templist)
            
strs = ''
path = "D:\Capstone\Prediction Dataset\*.txt"
files = glob.glob(path)
nlp = spacy.load("en_core_web_sm")
count = 0
keywords = ["contacted","veto","join","left","sanctions","sue","competition","competitor","acquires","scooped","partnership","develop","registered","sell","purchased","market","bought","demerger","announced","brand","own","supplies","subsidiary","merger","supplier","supply","promotion","acquisition","application","app","deal","agreement","takeover","apps","service","loan"]
keywords_nlp = []
for x in keywords:
    x = nlp(x)
    for token in x:
        #print(token.lemma_)
        keywords_nlp.append(token.lemma_)
print(keywords_nlp)
#print(keywords)
count1 = 0
#f = open("newsdataset1.txt","r")
#f = open("articles1.txt","r",encoding="utf8")
#f = open("rawtestdata.txt","r")
#print(files)
#f = open("testdoc1.txt","r")
#strs = f.read()
for f in files:
    file_obj = open(f,"r",encoding = "utf8")
    #print("here")
    count1 = count1+1
    #print("HEREE",count1)
   # strs = file_obj.read()
    #print(strs)
    #print(strs)
    #doc1 = nlp(strs)
   # for line in doc1.sents:
    for line in file_obj:
        #print("here",line)
        doc = nlp(line);
        #for token in doc:
         #   print(token.text, token.lemma_, token.pos_, token.tag_,
          #        token.shape_, token.is_alpha, token.is_stop)
        #for ent in doc.ents:
         #   print(ent.text, ent.start_char, ent.end_char, ent.label_)
        #displacy.serve(doc, style="dep")
        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj"), 
                                        AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       AnyPipe([FindTokensPipe("VERB/advcl/VERB"),
                                FindTokensPipe("VERB/revcl/VERB")]),
                       SequencePipe([FindTokensPipe("VERB/dobj/*/relcl/VERB/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('1',a)
            list_create(a,line,finallist)
            print("\n")
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/NOUN/poss/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/dobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/dobj/NOUN/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('2',a)
            list_create(a,line,finallist)
            print("\n")
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/NOUN/compound/PROPN"),
                                       AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       AnyPipe([FindTokensPipe("VERB/advcl/VERB"),
                                FindTokensPipe("VERB/revcl/VERB")]),
                       SequencePipe([FindTokensPipe("VERB/nsubj/NOUN/appos/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('3',a)
            list_create(a,line,finallist)
            print("\n")
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubjpass/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/prep/ADP/pobj/NOUN/acl/VERB/dobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/prep/ADP/pobj/NOUN/acl/VERB/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                        # NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('4',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/dobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/dobj/NOUN/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('5',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                        # NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/dobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('6',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       AnyPipe([FindTokensPipe("PROPN/acl/VERB/dobj"),
                                FindTokensPipe("PROPN/relcl/VERB/dobj"),
                                FindTokensPipe("PROPN/advcl/VERB/dobj")]),
                       SequencePipe([AnyPipe([FindTokensPipe("PROPN/acl/VERB/prep/ADP/pobj/NOUN/compound/PROPN/compound/PROPN"),
                                             FindTokensPipe("PROPN/relcl/VERB/prep/ADP/pobj/NOUN/compound/PROPN/compound/PROPN"),
                                             FindTokensPipe("PROPN/advcl/VERB/prep/ADP/pobj/NOUN/compound/PROPN/compound/PROPN"),
                                              FindTokensPipe("PROPN/relcl/VERB/prep/ADP/pobj/NOUN/compound/PROPN"),
                                              FindTokensPipe("PROPN/relcl/VERB/prep/ADP/pobj/PROPN")]),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('7',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/xcomp/VERB/prep/ADP/pobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/xcomp/VERB/dobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('8',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        

        pipes_structure = [SequencePipe([AnyPipe([FindTokensPipe("PROPN"),
                                             FindTokensPipe("VERB/relcl/PROPN"),
                                             FindTokensPipe("VERB/advcl/PROPN")]),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/xcomp/VERB"),
                       SequencePipe([FindTokensPipe("VERB/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('100',a)
            print("\n")
            if a[0][1] in keywords:
                print("YY\n")
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB"),
                       SequencePipe([FindTokensPipe("VERB/dobj/NOUN/poss/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('9',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB"),
                       SequencePipe([FindTokensPipe("VERB/dobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('11',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        #Salesforce made its biggest ever acquisition in March agreeing to pay $6.5 billion in a cash and stock deal for MuleSoft

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/dobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/**/VERB/prep/ADP/pobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('11',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        #Salesforce made its biggest ever acquisition in March agreeing to pay $6.5 billion in a cash and stock deal for MuleSoft

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB"),
                       SequencePipe([FindTokensPipe("VERB/dobj/PROPN/conj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                         #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('12',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        #Popular job search and company review site Glassdoor was acquired in May for an eye-popping all-cash $1.2 billion by Recruit Holdings

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubjpass/NOUN/appos/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB"),
                       SequencePipe([FindTokensPipe("VERB/prep/ADP/**/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"), 
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('13',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/dobj/NOUN/poss/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/dobj/NOUN"),
                       SequencePipe([FindTokensPipe("VERB/dobj/NOUN/prep/ADP/**/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"), 
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('14',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        #Oracle announced that it had agreed to acquire Datascience.com in May

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB/**/VERB"),
                       SequencePipe([FindTokensPipe("VERB/**/VERB/dobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"), 
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('15',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)

        #PayPal acquired Swedish fintech firm iZettle for $2.2 billion in May, giving the payments giant a popular point-of-sale (PoS) technology solution to add to its portfolio

        pipes_structure = [SequencePipe([FindTokensPipe("VERB/nsubj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"),
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()]),
                       FindTokensPipe("VERB"),
                       SequencePipe([FindTokensPipe("VERB/dobj/PROPN"),
                                     AggregatePipe([NamedEntityFilterPipe("GPE"),
                                                    #NamedEntityFilterPipe("PERSON"), 
                                                NamedEntityFilterPipe("ORG")]),
                                     NamedEntityExtractorPipe()])]
                   
        engine = PipelineEngine(pipes_structure, Context(doc), [0,1,2])
        try:
            a = engine.process()
        except IndexError:
            pass
        if a:
            print('16',a)
            print("\n")
            list_create(a,line,finallist)
            count = count + 1
            print(count)
            
f = open("finaldata2.csv","a",encoding = "utf8")
flag = 0
f.write("\n")
for i in finallist:
    #print(i[3])
    i[3] = i[3].translate({ord(","):None})
    #print(i[3])
    f.write(i[0]+","+i[1]+","+i[2]+","+i[3]+"\n")
    #print("here")
f.close()

        


#LG LG PROPN NNP XX True False
#Electronics Electronics PROPN NNP Xxxxx True False
#has have VERB VBZ xxx True True
#signed sign VERB VBN xxxx True False
#a a DET DT x True True
#deal deal NOUN NN xxxx True False
#to to PART TO xx True True
#supply supply VERB VB xxxx True False
#vehicle vehicle NOUN NN xxxx True False
#parts part NOUN NNS xxxx True False
#for for ADP IN xxx True True
#Tata Tata PROPN NNP Xxxx True False
#Motors Motors PROPN NNP Xxxxx True False
#LG Electronics 0 14 ORG
#Tata Motors 61 72 ORG
#Tata 128 132 ORG
#LG 151 153 ORG
#Tata Motors 207 218 ORG
#nearly 80 percent 481 498 PERCENT
#Tata Hitachi 551 563 LOC
#Honeywell 692 701 ORG
#Tata Hitachi 728 740 GPE
#Pune   934 940 GPE
#Tata Hitachi’s 1003 1017 FAC
#three 1018 1023 CARDINAL
#India 1024 1029 GPE
#about 45 1111 1119 CARDINAL
#India 1142 1147 GPE
#36 1149 1151 CARDINAL
#9 1163 1164 CARDINAL
#three 1183 1188 CARDINAL
#IPD 1245 1248 ORG
#    Toyota Toyota PROPN NNP Xxxxx True False
#supplier supplier NOUN NN xxxx True False
#Toyotetsu Toyotetsu PROPN NNP Xxxxx True False
#expanding expand VERB VBG xxxx True False
#in in ADP IN xx True True
#Ontario Ontario PROPN NNP Xxxxx True False
#to to PART TO xx True True
#supply supply VERB VB xxxx True False
#new new ADJ JJ xxx True False
#Lexus Lexus PROPN NNP Xxxxx True False
#RAV4 RAV4 PROPN NNP XXXd False False
#Toyota 0 6 ORG
#Toyotetsu 16 25 ORG
#Ontario 39 46 GPE
#[]
#Lexus 61 66 ORG
#[]
