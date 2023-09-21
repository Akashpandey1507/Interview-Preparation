import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:/ConsoleFlare/MLDataToBeSent/Salary_Data.csv")

sns.jointplot(data=df,x="YearsExperience",y="Salary")
plt.show()

X=df["YearsExperience"]
y=df["Salary"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=50)

print(X_train)
print("****************")
print(X_test)
print("****************")
print(y_train)
print("****************")
print(y_test)
print("****************")