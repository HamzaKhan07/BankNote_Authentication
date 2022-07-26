import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv("BankNote_Authentication.csv")
print(df.tail())

# Independent and Dependent features
x=df.iloc[:, :-1]
y=df.iloc[:, -1]

# test and split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Implement Random Forest Classifier
classifier=RandomForestClassifier()
classifier.fit(X_train, Y_train)

# Prediction
Y_pred= classifier.predict(X_test)

# Check accuracy
score=accuracy_score(Y_test, Y_pred)
print(score)

# custom prediction
# cust_pred=classifier.predict([[2,3,4,1]])
# print(cust_pred)

# Save model
# joblib.dump(classifier, 'classifier.pkl')
# print('model saved')

# Load model
saved_classifier=joblib.load('classifier.pkl')
saved_pred=saved_classifier.predict([[-2,0.6,2,1]])
print(saved_pred[0])






