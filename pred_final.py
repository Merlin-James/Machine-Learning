import numpy as np
import pandas as pd
from pandas_ml import ConfusionMatrix
import matplotlib.pyplot as plt
from pandas import read_csv
#The Machine learning alogorithm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt 
from sklearn.metrics import roc_curve, auc
# Test train split
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
# Just to switch off pandas warning
pd.options.mode.chained_assignment = None

# Used to write our model to a file
from sklearn.externals import joblib

data = read_csv("data.csv")
test_input = data[["Duration", "packet", "byte length"]]
test_output = data[["result"]]
rf = joblib.load("test_model1")
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

# Plot of a ROC curve for a specific class
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()

y= np.array(pred)
if(np.count_nonzero(y==1))>8:
    print "Attack Detected"
else:
    print "No Attack"
    

