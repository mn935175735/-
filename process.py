# -*- coding:utf-8 -*-
import json
import sys
import os
import jieba
import jieba.posseg
import jieba.analyse
import Synonym

def bulitDict(dirname):
    word = json.load(dirname + '/words.json')
    degree = json.load(dirname + "/degree.json")
    d = {}

    for x in word:
        d[x['word']] = x['value']

    for x in degree:
        d[x['word']] = x['wordvalue']

    return d



def main(dirname):
    wordList = bulitDict(dirname + '/dict')

    synonymDict = Synonym.Synonym(dirname + "/dict/words.vector")

    value = []

    stopWord = []
    with open(dirname + "/dict/stopword.txt", "r") as f:
            while 1:
                line = f.readline()
                if not line:
                    break
                stopWord.append(line)

    files = os.listdir(dirname + '/data')
    for filename in files:
        data = json.load(dirname + "/data" + filename)
        for cmt in data:
            cmt_seg = jieba.posseg.cut(cmt['text'])

            print(cmt_seg)

            cmt_value = 1

            for seg in cmt_seg:
                if seg in stopWord:
                    continue
                try:
                    score = wordList[seg.word]
                except:
                    print("Word " + seg.word + " is not in the nornaml dict. Searching in the synonym...")
                    try:
                        syno = synonymDict.get_synonym(seg.word)
                        score = wordList[syno[0]] * syno[syno[1]]
                    except:
                        print("Word " + seg.word + " POS " + seg.flag)
                cmt_value *= score
            
            value.append(cmt_value)
    

if __name__ == "__main__":
    main(sys.argv[1])