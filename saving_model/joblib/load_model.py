import joblib
#load model
model=joblib.load('diabetic_79.pkl')
result=model.predict([[1,1,1,1,1,1,1,1]])#xtest only accept 2d
print(result)
if result[0] == 1:
    print('Person is diabetic')
else:
    print('not diabetic')