# weibo-ner-conll
去除weiboNER_2nd_conll数据集的分词信息，只保留实体信息，制作成conll格式。

## 使用说明

可以直接

## 说明

WeiboNER数据集可以从[golden-horse](https://github.com/hltcoe/golden-horse/tree/master/data)下载，里面包含weiboNER和weiboNER_2nd_conll两版数据集，在[FLAT](https://github.com/LeeSureman/Flat-Lattice-Transformer)论文里用的是第二版数据集。

weiboNER只包含实体信息，如下：

```
口	O
腔	O
溃	O
疡	O
加	O
上	O
这	O
玩	O
意	O
～	O
酸	O
酸	O
甜	O
甜	O
好	O
滋	O
味	O
。	O
```

而weiboNER_2nd_conll里除了包含实体信息，还包含分词信息，如下：

```
口0	O
腔1	O
溃2	O
疡3	O
加0	O
上1	O
这0	O
玩0	O
意1	O
～0	O
酸0	O
酸1	O
甜2	O
甜3	O
好0	O
滋0	O
味1	O
。0	O
```

为了能够在[FLAT](https://github.com/LeeSureman/Flat-Lattice-Transformer)里直接使用weiboNER_2nd_conll数据集，需要删除
