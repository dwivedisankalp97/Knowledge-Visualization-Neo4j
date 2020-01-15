# Knowledge-Visualization-Neo4j
Knowledge visualization from news articles using a graph database

The main objective of this project is to ease the process of extracting information from news articles. The tasks to be completed are
a.)	Classifying the data with machine learning.
b.)	Extraction of relevant entities from the dataset.
c.)	Creating a graphical database to showcase the relationships between entities.

The project is be created using python and neo4j. . First, through python and scikit-learn machine learning library, we will detect the presence of relationships in pre-processed news articles. Then, using Spacy NLP library we will extract the relevant entities such as people, places and other nouns that are present in the document. The relationship will be determined through dependency parsing, such as if two people are mentioned in the same document, we need to identify the relationship between two people in order to store them in the graph property model. Then, through python scripts, we will create a neo4j database that includes the relationships between entities.

1.	Python	3.6	
2.	Spacy	2.0	
3.	Numpy	1.16.2	
4.	NLTK	3.4
5.	Scikit-learn	0.20.2	
6.	Textpipeliner	1.0
7.	Grammaregex	1.0	
8.	Neo4j	3.5.1 

PROJECT PHASES AND COMPONENTS

The development of this project was broken down into several phase, each equally important to generate the best result possible. The phases are listed below and delineated further in the section.
-	Labeled dataset preparation
-	Training and testing classification model
-	Writing rules for dependency parser.
-	Using Textpipeliner
-	Creating the database

Training and testing classification model
To convert the text into features, we have used TF-IDF, short for Term Frequency – Inverse Data Infrequency. It has the following components
-	Term Frequency: It gives us the frequency of the word in each document in the data. It is the ratio of number of times the word is present in a document compared to the total number of words in that document. It increases as the number of occurrences of that word within the document increases.
 
-	Inverse Data Frequency: It is used to calculate the rarity of a word in a document. Words that appear rarely in the data have a high IDF score.
 
We get TF-IDF from the product for TF and IDF.
 
We will use TF-IDF vectorizer provided by scikit-learn.

Tfidf_vect = TfidfVectorizer (ngram_range= (1, 4))

Tfidf_vect.fit (Corpus ['text_final'])

For the purpose of learning, the model was tested on several machine learning algorithm such as Decision Trees, SVM and Naïve Bayes. We got consistently higher accuracy using SVM, which was ultimately selected as the learning algorithm for our model.

Testing was done by splitting the labelled dataset into testing data and training data. Training data consisted of 70% of the document and the rest was left for testing. During testing, we got accuracy in the range of 80% to 89%, which is good enough for our purpose, as we will be dealing with large amounts of data.

Writing rules for Dependency Parser

Dependency parser analyzes the grammatical structure of the sentence, identifying relationships between head words and words which modify these head words. An example of dependency parser is given below.

Example 1: Microsoft has reached an agreement to acquire GitHub
 

Figure 3 – Dependency Tree for Example 1


In order to extract the relations, we need to traverse the dependency tree of the sentence and identify the verb, subject and object. This is done by writing rules for tree traversing. The root of a DP tree is the main verb of the sentence. For example, in the Example 1, we need the output to be (Microsoft, acquire, Github). As we can see that the root node of the DP tree is the verb “reached”, but the relation we have to extract is “acquire”. To extract the required relation, we will have to write a rule in the regular expression. For Example 1, the rules will be the following.

(("VERB/nsubj/PROPN"), ("VERB/**/VERB"), ("VERB/**/VERB/dobj/PROPN"))

Traversing the tree with these rules will give us the following output.

(Microsoft, [has, acquire], Github)

The output contains an unnecessary relation “has”. To filter out such relations, we have to create a list of keywords, containing only the relations that we need. We have used the following keywords.

-	Contact
-	Veto
-	Join
-	Leave
-	Sanction
-	Sue
-	Competition
-	Competitor
-	Acquire
-	Scoop
-	Partnership
-	Develop
-	Register
-	Sell
-	Purchase
-	Market
-	Buy
-	Demerger
-	Announce
-	Brand
-	Own
-	Supply
-	Subsidiary
-	Merger
-	Supplier
-	Supply
-	Promotion
-	Acquisition
-	Application
-	App
-	Deal
-	Agreement
-	Takeover
-	App
-	Service
-	Loan


After passing the filter of keywords, we get the following output,

Output 1: (Microsoft, acquire, Github)

Which is the desired relation.

Another measure put in place to root out negative matches is Named Entity Resolution. NER is the process of locating and classifying named entities present in the document. For Example 1, we get the following output after running NER.

Microsoft 0 9 ORG

GitHub 46 52 ORG

This signifies that Microsoft and Github are both organizations. 

We have to incorporate NER into our relationship extractor to make sure that we only get relations between organizations and countries. The next section will describe how we will combine dependency parser and NER together with the help of a python library.

Textpipeliner

Textpipeliner is an efficient library for extracting relation using dependency parsing and NER. 
For Example 1, textpipeliner code is given below.

pipes_structure = [SequencePipe ([FindTokensPipe ("VERB/nsubj/PROPN"),
                                     AggregatePipe ([NamedEntityFilterPipe ("GPE"),
                                                NamedEntityFilterPipe ("ORG")]),
                                     NamedEntityExtractorPipe ()]),
                       FindTokensPipe ("VERB/**/VERB"),
                       SequencePipe ([FindTokensPipe ("VERB/**/VERB/dobj/PROPN"),
                                     AggregatePipe ([NamedEntityFilterPipe ("GPE"), 
                                                NamedEntityFilterPipe ("ORG")]),
                                     NamedEntityExtractorPipe ()])]


Creating the database
While feeding the database, we need to make sure that all the nodes are unique and no redundant nodes are present. Neo4j provides us with an easy way to make sure that such conditions are specified through the MERGE command.
The template for MERGE commands is 
MERGE (u: entitity {name:’ ENTITY 1'}) 
MERGE (l: entitity {name:' ENTITY 2'}) 
MERGE (u) - [: RELATIONSHIP ]-> (l)
MERGE command is a combine form of MATCH and CREATE commands. First, the MERGE command searches for a match for the entity specified. If a match is found, it assigned a temporary pointer “u” for that entity. If a match is not found, it will create a node for that entity. The same command is used to assign a pointer of ENTITY 2. The third MERGE command searches for a match for the relationship between entities. If a match is not found, the relationship is inputted into the database. 

