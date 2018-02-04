import numpy as np
import pandas as pd

from pandas import read_csv
#The Machine learning alogorithm
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Test train split
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
# Just to switch off pandas warning
pd.options.mode.chained_assignment = None

# Used to write our model to a file
from sklearn.externals import joblib

data = read_csv("tableset.csv")
print data.head()
print data.columns
data_inputs = data[["Duration", "No. of packets", "Byte length"]]
print data_inputs.head()

ex_outputs = data[["result"]]
print ex_outputs.head()

rf = RandomForestClassifier (n_estimators=20)
rf.fit(data_inputs, ex_outputs)
accuracy = rf.score(data_inputs, ex_outputs)
print "Accuracy = {}%".format(accuracy * 100)
joblib.dump(rf, "test_model1", compress=9)

importances = rf.feature_importances_
indices = np.argsort(importances)
 
plt.figure(1)
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), data_inputs[indices])
plt.xlabel('Relative Importance')
plt.show()
