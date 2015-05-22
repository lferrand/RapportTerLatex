import os
import collections

stop_words = [ word for word in open("C:\\stop_words.txt", 'r') ]

def deleteStopWords(in_path,out_path):
    #Repertoire contenant tous les fichiers utilisateurs
    reviewNames = (os.listdir(in_path))
    for review in reviewNames:
        #Parcours de tous les utilisateurs un a un
        infile = in_path + review
        outfile = out_path + review
        fin = open(infile)
        fout = open(outfile, "w+")
        for line in fin:
            for word in stop_words:
                line = " "+line+" "
                line = line.lower().replace("."," ").replace(","," ").
                                    replace(";"," ").replace("'","").
                                    replace("!"," ").replace("("," ").
                                    replace(":"," ").replace(")"," ").
                                    replace("#"," ").replace("/"," ");
            line = line.replace("\n"," ")
            line = line.replace(" "+word+" "," ").strip()+" "
            print(line)
        fout.write(line)
    fin.close()
    fout.close()
# Test to delete stop words
deleteStopWords(r"C:\\Users\\Jiaff\\Desktop\\NLTK\\Horrible\\",
                r"C:\\Users\\Jiaff\\Desktop\\NLTK_CLEANED\\Horrible\\");