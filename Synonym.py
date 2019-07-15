import gensim.models.word2vec

class Synonym:

    def __init__(self, filename):
        self.w2v = gensim.models.Word2Vec.load(filename)

    def get_synonym(self, word):
        try:
            sim_word = self.w2v.most_similar(word, topn=1)
        except:
            print("Cannot find the synonym of " + word + "!!!")
        return sim_word