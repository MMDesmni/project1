# Importing libraries we need

import pandas as pd
import matplotlib as plt
import scipy.stats as stats

# In this part we read the file and transform it into csv(beacuase it is smoother to work with)
file_name="Orders.xlsx"
df=pd.read_excel(file_name)
df.to_csv("Orders_output.csv",index=False)

#adding an extra row

df["status"]="Recived"
df["order_way"]="online"

#these variables would be used in following
h=0
l=0

#First we have an outlook to our DataFrame
df.info()

# We get some basic information(these lines give us the first 10 and last 10 rows do DataFrame)
print("Our first 10 orders are : "+df.head(10))
print("Our last 10 orders are : "+df.tail(10))
print("Our number of succesful orders are : "+df.dropna(inplace=True))
print("Our number of missed information in every order is : "+df.isna().sum())
print("Highest value order is : "+df.max())
print("Lowest value order is : "+df.min())
print("Average Value of orders are : "+df.mean())
print("Range of orders are from"+df.min()+"to"+df.max())
print("Our feature of orders are : "+df.columns())
print("Our order informations are : "+df.index())
print("Number of orders that were registered are : "+df.duplicated().sum())



#this method is not good for organizing the data that we have
df.drop(columns='country',inplace=True)
df.fillna(method="ffill",inplace=True)
df.fillna(method="bfill",inplace=True)

# in this part wwe are trying to organize our data and update them with the mean that we have
df.drop(columns='country',inplace=True)
df.fillna(df.mean(),inplace=True)
df["value"] = pd.to_numeric(df["value"], errors="coerce")
df['number']=pd.to_numeric(df["number"],errors="coerce")
df = df.drop_duplicates(subset="value")



#now that our data is more orginized we could use the math formulas we have
print(df.describe())

#now we wanna look at our datas under Circumstance and have them
try:
    print(df["value"]>=350)
except ValueError:
    print("These are not int type and could not be used")

if(df["value"]>=df.mean()):
    h+=1
elif(df["value"]<=df.mean()):
    l+=1
else:
    pass

print(f"Number of high value orders are {h} and number of low value orders are {l}")

#We want to find data of our highest/lowest customer

print(df.where(df["value"]==df["value"].max()).dropna['country'])
print(df.where(df["value"]==df["value"].max()).dropna['name'])
print(df.where(df["value"]==df["value"].min()).dropna['contry'])
print(df.where(df["value"]==df["value"].min()).dropna['name'])
print(df.where(df["number"]==df["number"].max()).dropna['country'])
print(df.where(df["number"]==df["number"].max()).dropna['name'])
print(df.where(df["number"]==df["number"].min()).dropna['contry'])
print(df.where(df["number"]==df["number"].min()).dropna['name'])



#Now we wanna return and print some rows just by giving the row number

print(df[['name','country','value']].iloc[[0,15,11,17]].where(df['value']>=100))
print(df['name'].iloc[3])
print(df['value','country'].iloc[14,8,6,2])

