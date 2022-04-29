import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_curve, accuracy_score, roc_auc_score 

class machinelearning :
    def __init__(self, model_name, train_x, train_y, test_x, test_y) :
        self.__model__name = model_name
        self.__train_x = train_x
        self.__train_y = train_y
        self.__test_x = test_x
        self.__test_y = test_y

    def set_model(self, model):
        self.__model = model

    def model_predict(self, test_x):
        self.__predict = self.__model.predict(test_x).reshape(-1)
        self.__y_pred = [round(pred) for pred in self.__predcit]
        print('Done') 

    def roc(self) :

        thresholds = np.arange(1, 0, -0.01)
        self.__fpr = []
        self.__tpr = []
        for threshold in thresholds :
            fp = 0
            tp = 0
            an = 0
            ap = 0
            clf = [1 if predict > threshold else 0 for predict in self.__predict]

            for idx in range(len(clf)) :
                pass