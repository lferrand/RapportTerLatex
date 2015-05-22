import nltk
import os

pattern_grammar = "CHUNK: {<JJ.*>+<NN.*>}"

def ie_preprocess(document):

    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    taggers = list()
    for sent in sentences:
        taggers.extend(nltk.pos_tag(sent))

    parser = nltk.RegexpParser(pattern_grammar)
    tree = parser.parse(taggers)
    data = "";
    for subtree in tree.subtrees():
        if subtree.node == 'CHUNK':
            for (v,t) in subtree.leaves():
                data += v + " ";

    return data

def preprocesing(inpath,outpath):
    array_files = [ f for f in os.listdir(inpath) 
            if os.path.isfile(os.path.join(inpath,f)) ]
    for file in array_files:
        buff = ""
        for line in open(os.path.join(inpath,file),'r'):
            buff +=  line;

        file = open(os.path.join(outpath,file), 'w+')
        file.write(ie_preprocess(buff))
        file.close()

# Test to execute the pattern grammar: Adjetive+ Noun(singular/plural)
preprocesing("/Users/user/.../AVIS_HOTELS_Tripadvisor2/Moyen/",
    "/Users/user/.../AVIS_HOTELS_Tripadvisor2/Moyen_CLEAN/")
