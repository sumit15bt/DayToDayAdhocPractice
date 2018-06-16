from sklearn import tree
import os
# apple=0,orange=1
data=[[100,0],[135,0],[135,1],[160,1]]
output=["apple hai","apple hai","orange hai","orange  hai"]
algo=tree.DecisionTreeClassifier()
train_algo=algo.fit(data,output)
weight=input("enter weight of fruit")
surface=input("enter 0 smooth and 1 for rough ")
predict=train_algo.predict([[weight,surface]])
os.system("echo $predict|festival --tts")
print(predict)
