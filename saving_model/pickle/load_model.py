import pickle
#load model
model=pickle.load(open('diabetic_79.sav','rb'))
result=model.predict([[1,1,1,1,1,1,1,1]])#xtest only accept 2d
print(result)
if result[0] == 1:
    print('Person is diabetic')
else:
    print('not diabetic')