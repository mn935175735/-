# isArknightsGood

This project is a team-work project for CS190B in ShanghaiTech.
The data in this project is mainly from Weibo and Bilibili.

## usage

### training word2vec model

    python trainSynonym.py <filename>

file should be in json format like

    [
        {
            date: ...,
            text: "This is a string",
            ...
        },
        ...
    ]

## using package

gensim.model.word2vec

@online{Synonyms:hain2017,
  author = {Hai Liang Wang, Hu Ying Xi},
  title = {中文近义词工具包Synonyms},
  year = 2017,
  url = {https://github.com/huyingxi/Synonyms},
  urldate = {2017-09-27}
}

jieba