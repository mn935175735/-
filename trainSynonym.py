import gensim
import json
import sys
import jieba
import os

if __name__ == "__main__":
    model = gensim.models.Word2Vec(min_count=1, size=500, workers=8)
    dirname = sys.argv[1]
    files = os.listdir(dirname)
    for filename in files:
        print('Handle file: ' + filename)
        with open(dirname + '/' + filename, encoding='utf-8') as f:
            data = json.load(f)
            #print(data)
        

        stopWord = ['.', '?', '!', '\n', '。', '？', '！', '…']
        """ with open("./stopword.txt", "r") as f:
            while 1:
                line = f.readline()
                if not line:
                    break
                stopWord.append(line) """

        sentences = []
        for cmt in data:
            cmt_seg = jieba.cut(cmt['text'])
            sentence = []
            for word in cmt_seg:
                if word in stopWord:
                    if len(sentence) > 0:
                        sentences.append(sentence)
                    sentence = []
                else:
                    sentence.append(word)
        model = gensim.models.Word2Vec.load('train_data/words.vector')
        # model.build_vocab(sentences)
        model.train(sentences, total_examples=len(sentences), epochs=model.epochs)

        model.save('train_data/words.vector')
        print('Model saved...')
