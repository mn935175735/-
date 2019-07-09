import gensim
import json
import sys
import jieba

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, encoding='utf-8') as f:
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
        print(cmt['text'])
        cmt_seg = jieba.cut(cmt['text'])
        sentence = []
        for word in cmt_seg:
            if word in stopWord:
                if len(sentence) > 0:
                    sentences.append(sentence)
                    print(sentence)
                sentence = []
            else:
                sentence.append(word)
    model = gensim.models.Word2Vec(min_count=1, size=500, workers=8)
    model.build_vocab(sentences)
    model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)

    model.save(filename.split('.')[0])
