# isArknightsGood

This project is a team-work project for CS190B in ShanghaiTech.
The data in this project is mainly from Weibo and Bilibili.

## usage

### training word2vec model

    python trainSynonym.py <dirname>

The script while handle the json files in <i> dirname </i> should be in json format like

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

jieba

data from synonym
