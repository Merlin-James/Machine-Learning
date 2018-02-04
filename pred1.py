import numpy as np
import pandas as pd

from pandas import read_csv
#The Machine learning alogorithm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt 
 
# Test train split
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
# Just to switch off pandas warning
pd.options.mode.chained_assignment = None

# Used to write our model to a file
from sklearn.externals import joblib
data = read_csv("data2.csv")
test_input = data[["Duration", "tp_src", "tp_dst", "byte length"]]
test_output = data[["result"]]
rf = joblib.load("test_model")
pred = rf.predict(test_input)
print pred
accuracy = rf.score(test_input, test_output)
print "Accuracy = {}%".format(accuracy * 100)
results = confusion_matrix(pred, test_output)
print "----Confusion Matrix-----"

print results
plt.matshow(results)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('Actual')
plt.xlabel('Predicted')
#plt.show()

#calculate TPR, FPR
fpr,tpr, _ = roc_curve(test_output, rf.predict_proba(test_input)[:,1])

roc_auc = auc(fpr, tpr)
print 'ROC AUC: %0.2f' % roc_auc

#plot ROC
plt.figure()


y= np.array(pred)
if(np.count_nonzero(y==1))>8:
    print "Attack Detected"
else:
    print "No Attack"
    

