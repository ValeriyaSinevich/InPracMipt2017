

import requests
import os
import subprocess
import glob


class Kea_keyword_extractor:
    def __init__(self, kea_path='/home/valeriyasin/Programms/kea-5.0_full',                 train_path ='/home/valeriyasin/Documents/train_documents', test_path="/home/valeriyasin/Documents/test_docs"):
        self.kea_path = kea_path
        self.train_path = train_path
        self.test_path = test.path
    def setup_java(self):
        os.environ["KEAHOME"] = self.kea_path
        os.environ["CLASSPATH"] = "{0}:{0}/lib/commons-logging.jar:{0}/lib/icu4j_3_4.jar:{0}/lib/iri.jar:"            .format(os.environ["KEAHOME"])  +             "{0}:/lib/jena.jar:{0}/lib/snowball.jar:{0}/lib/weka.jar:{0}/lib/xercesImpl.jar:{0}/lib/kea-5.0.jar"            .format(os.environ["KEAHOME"])
#     print(os.environ["KEAHOME"], os.environ["CLASSPATH"])
        
    def train_model(self):
        curpath = os.getcwd()
        os.chdir(self.kea_path)
        setup_java()
        os.system("java -Xmx526M TestKea train " + self.train_path + "> out.txt 2> err.txt")
    #     print("out", open("out.txt").read(), "err", open("err.txt").read())
        os.chdir(curpath)
    def extract_keywords(self):
        extracted_keywords = []
        for file in glob.glob(self.test_path + "/*.key"):
            os.system("rm " + file)
        
        curpath = os.getcwd()
        os.chdir(self.kea_path)
        
        os.system("java -Xmx526M TestKea test " + elf.test_path)
        os.chdir(curpath)
        for file in glob.glob(self.test_path + "/*.key"):
            f = open(file)
            for line in f:
                extracted_keywords.append(line)
            f.close()
        return extracted_keywords

    def train(self, texts, keywords):
      
        for idx, text in enumerate(texts):
            text_file = open(self.train_path + "/" + "text{}.txt".format(idx), "w")
            text_file.write(text);
            key_file = open(self.train_path + "/" + "text{}.key".format(idx), "w")
            key_file.write(keywords[idx]);
            text_file.close()
            key_file.close()
            setup_java()
            train_model(self.train_path)
    def predict(self, texts):
        words = []
        for idx, text in enumerate(texts):
            text_file = open(self.test_path + "/" + "text{}.txt".format(idx), "w")
            text_file.write(text);
            text_file.close()
            extracted_word = extract_keywords(self.test_path) 
            words.append(self.test_path)
        return words



