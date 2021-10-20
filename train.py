import os
from sklearn.feature_extraction.text import TfidfVectorizer as TF
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer as TF
from sklearn.feature_extraction.text import CountVectorizer as CF
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.metrics import accuracy_score
from joblib import dump

def extract_file(dir):
    allfiles=[]
    for root, dirs, files in os.walk(dir):
        for filename in files:
            # list filenames
            # get the absolute path for the files
            AbsolutePath = os.path.join(root, filename)
            # get the absolute path for the files

            if filename.endswith("txt"):
                allfiles.append(AbsolutePath)

    return allfiles
print(extract_file("features"))
FeatureVectorizer = CF(input="filename", tokenizer=lambda x: x.split('\n'), token_pattern=None,
                           binary=True)
mal_features=extract_file("res/malware")
good_features=extract_file("res/benign")
x_train = FeatureVectorizer.fit_transform(mal_features + good_features)
print x_train
mal_labels=np.ones(len(mal_features))
good_labels=np.empty(len(good_features))
good_labels.fill(-1)

y_train = np.concatenate((mal_labels, good_labels), axis=0)

Parameters= {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}

Clf = GridSearchCV(LinearSVC(max_iter=1000000), Parameters, cv= 5, scoring= 'f1', n_jobs=-1 )
SVMModels= Clf.fit(x_train, y_train)

BestModel= SVMModels.best_estimator_
dump(Clf, "svmmodel.pkl")
