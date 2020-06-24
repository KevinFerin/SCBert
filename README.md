# Sentence Clustering with BERT (SCB)

Sentence Clustering with BERT project which aim to use state-of-the-art BERT models to compute vectors for sentences. A few tools are also implemented to explore those vectors and how sentences are related to each others in the latent space. 

### Demonstration 

- **Load example data set :**
```
from SCBert.load_data import DataLoader

cls = DataLoader().load_cls_fr()
data = cls.review
```


- **Create vectors from raw data :**

```
#How to transform raw french texts into vectors using BERT model. 
from SCBert.SCBert import Vectorizer

vectorizer = Vectorizer("flaubert_small")
#Here the small version of FLauBERT only has 6 layers and we will take layers 4 and 5 and mean pool them to create 
#a vector for each word, then mean pool all words vectors to have a unique vector for each text
text_vectors = vectorizer.vectorize(data, layers=[4,5], word_pooling_method="average", sentence_pooling_method="average")
```

- **Explore the embedded space :**
```
#How to explore the relation in your data. 
from SCBert.SCBert import EmbeddingExplorer

ee = EmbeddingExplorer(data,text_vectors)
labels = ee.cluster(k=3,  cluster_algo="quick_k-means")     #Cluster with k-means 
ee.extract_keywords(num_top_words=15)                       #Extract 15 keywords using Rake algorithm, then accessible with ee.keywords
ee.compute_coherence(vectorizer)                            #Compute coherence for the keywords in each cluster
ee.explore_cls(color_label=cls.code, 'PCA')                              #This function is here to explore a the repartition of cluster in the FULL cls dataset 
```

### Built-in example

There is a built-in example that you can find [here](examples/example_cls_fr.ipynb). It comes with it's own data which is the CLS-fr composed of Amazon reviews from different sources (DVD, CD, Livres)

### Installation 

You can either download the zip file or use the Pypi package that you can install with the following command : 

```
> pip install SCBert
```


If you encounter problems during the installation it may be because of the multi-rake dependy with cld2-cffi. I will try to address this later on. To bypass, just follow the instructions : 

```
> export CFLAGS="-Wno-narrowing"
> pip install cld2-cffi
> pip install multi-rake
```
