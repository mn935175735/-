# -*- coding:utf-8 -*-
import json
import sys
import jieba

def main(self, dirname):
    pAdvDict = json.load(dirname + '/pAdvDict.json')
    nAdvDict = json.load(dirname + '/nAdvDict.json')

    data = json.load(dirname + "weibo.json") + json.load(dirname + "bilibili.json")

    keyword = []
    with open(dirname + "/keyword.txt", "r") as f:
            while 1:
                line = f.readline()
                if not line:
                    break
                keyword.append(line)

    stopWord = []
    with open(dirname + "/stopword.txt", "r") as f:
            while 1:
                line = f.readline()
                if not line:
                    break
                stopWord.append(line)
    
    for cmt in data:
        cmt_seg = jieba.cut(cmt['text'])
        
    


if __name__ == "__main__":
    main(sys.argv[1])