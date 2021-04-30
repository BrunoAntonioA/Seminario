import data

import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import (NeighborhoodComponentsAnalysis, KNeighborsClassifier)

from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

dataTrain, trainLabel1, trainLabel2, trainShape = data.importDf("data/experimento-1-train-5000.csv")
dataTest, testLabel1, testLabel2, testShape = data.importDf("data/experimento-1-test-3000.csv")

#MLPClassifier neural network
origin_clf_mlpc = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
destiny_clf_mlpc = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
#train
origin_clf_mlpc.fit(dataTrain, trainLabel1)
destiny_clf_mlpc.fit(dataTrain, trainLabel2)
#predict
ori_clf_pred = origin_clf_mlpc.predict(dataTest)
dest_clf_pred = destiny_clf_mlpc.predict(dataTest)
#measure
ori_clf_acc_score = accuracy_score(testLabel1, ori_clf_pred)
ori_clf_recall = recall_score(testLabel1, ori_clf_pred, average='micro')
ori_clf_precision = precision_score(testLabel1, ori_clf_pred, average='micro', zero_division=1)
dest_clf_acc_score = accuracy_score(testLabel2, dest_clf_pred)
dest_clf_recall = recall_score(testLabel2, dest_clf_pred, average='micro')
dest_clf_precision = precision_score(testLabel2, dest_clf_pred, average='micro', zero_division=1)
#defining a row for the data set
ori_clf = { 
    'Model': 'Origin_clf_mlpc', 'Recall_score': ori_clf_recall, 'Acc_Score': ori_clf_acc_score,
    'Precission_score': ori_clf_precision
}
dest_clf = { 
    'Model': 'Destiny_clf_mlpc', 'Recall_score': dest_clf_recall, 'Acc_Score': dest_clf_acc_score,
    'Precission_score': dest_clf_precision

}

#GaussianNB
origin_gnb = GaussianNB()
destiny_gnb = GaussianNB()
#train and predict
y_ori_gnb_pred = origin_gnb.fit(dataTrain, trainLabel1).predict(dataTest)
y_dest_gnb_pred = destiny_gnb.fit(dataTrain, trainLabel1).predict(dataTest)
#measure
ori_gnb_acc_score = accuracy_score(testLabel1, y_ori_gnb_pred)
ori_gnb_recall = recall_score(testLabel1, y_ori_gnb_pred, average='micro')
ori_gnb_precision = precision_score(testLabel1, y_ori_gnb_pred, average='micro', zero_division=1)
dest_gnb_acc_score = accuracy_score(testLabel2, y_dest_gnb_pred)
dest_gnb_recall = recall_score(testLabel2, y_dest_gnb_pred, average='micro')
dest_gnb_precision = precision_score(testLabel2, y_dest_gnb_pred, average='micro', zero_division=1)
#defining a row for the data set
ori_gnb = { 
    'Model': 'Origin_gnb', 'Recall_score': ori_gnb_recall, 'Acc_Score': ori_gnb_acc_score,
    'Precission_score': ori_gnb_precision
}
dest_gnb = { 
    'Model': 'Destiny_gnb', 'Recall_score': dest_gnb_recall, 'Acc_Score': dest_gnb_acc_score,
    'Precission_score': dest_gnb_precision
}

#MNN-centroid
origin_NearCentroid = NearestCentroid()
destiny_NearCentroid = NearestCentroid()
#train
origin_NearCentroid.fit(dataTrain, trainLabel1)
destiny_NearCentroid.fit(dataTrain, trainLabel2)
#predict
ori_NearCentroid_pred = origin_NearCentroid.predict(dataTest)
dest_NearCentroid_pred = destiny_NearCentroid.predict(dataTest)
#measure
ori_NearCentroid_acc_score = accuracy_score(testLabel1, ori_NearCentroid_pred)
ori_NearCentroid_recall = recall_score(testLabel1, ori_NearCentroid_pred, average='micro')
ori_NearCentroid_precision = precision_score(testLabel1, ori_NearCentroid_pred, average='micro', zero_division=1)
dest_NearCentroid_acc_score = accuracy_score(testLabel2, dest_NearCentroid_pred)
dest_NearCentroid_recall = recall_score(testLabel2, dest_NearCentroid_pred, average='micro')
dest_NearCentroid_precision = precision_score(testLabel2, dest_NearCentroid_pred, average='micro', zero_division=1)
#defining a row for the data set
ori_NearCentroid = { 
    'Model': 'Origin_NearCentroid', 'Recall_score': ori_NearCentroid_recall, 'Acc_Score': ori_NearCentroid_acc_score,
    'Precission_score': ori_NearCentroid_precision
}
dest_NearCentroid = { 
    'Model': 'Destiny_NearCentroid', 'Recall_score': dest_NearCentroid_recall, 'Acc_Score': dest_NearCentroid_acc_score,
    'Precission_score': dest_NearCentroid_precision
}

#KNN
origin_knn = KNeighborsClassifier(n_neighbors=3)
destiny_knn = KNeighborsClassifier(n_neighbors=3)
#train
origin_knn.fit(dataTrain, trainLabel1)
destiny_knn.fit(dataTrain, trainLabel2)
#predict
ori_knn_pred = origin_knn.predict(dataTest)
dest_knn_pred = destiny_knn.predict(dataTest)
#measure
ori_knn_acc_score = accuracy_score(testLabel1, ori_knn_pred)
ori_knn_recall = recall_score(testLabel1, ori_knn_pred, average='micro')
ori_knn_precision = precision_score(testLabel1, ori_knn_pred, average='micro', zero_division=1)
dest_knn_acc_score = accuracy_score(testLabel2, dest_knn_pred)
dest_knn_recall = recall_score(testLabel2, dest_knn_pred, average='micro')
dest_knn_precision = precision_score(testLabel2, dest_knn_pred, average='micro', zero_division=1)
#defining a row for the data set
ori_knn = { 
    'Model': 'Origin_knn', 'Recall_score': ori_knn_recall, 'Acc_Score': ori_knn_acc_score,
    'Precission_score': ori_knn_precision
}
dest_knn = { 
    'Model': 'Destiny_knn', 'Recall_score': dest_knn_recall, 'Acc_Score': dest_knn_acc_score,
    'Precission_score': dest_knn_precision
}

df = pd.DataFrame(columns=['Model', 'Recall_score', 'Acc_Score', 'Precission_score'])
df = df.append(ori_clf, ignore_index=True )
df = df.append(ori_gnb, ignore_index=True )
df = df.append(ori_NearCentroid, ignore_index=True)
df = df.append(ori_knn, ignore_index=True)
df = df.append(dest_clf, ignore_index=True )
df = df.append(dest_gnb, ignore_index=True )
df = df.append(dest_NearCentroid, ignore_index=True)
df = df.append(dest_knn, ignore_index=True)

df.to_csv('sklear_results.csv')