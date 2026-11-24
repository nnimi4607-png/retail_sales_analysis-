import pandas as pd

df=pd.read_csv('C:/Users/simra/OneDrive/Desktop/Retail_Sales_Analysis/data/retail_sales_dataset.csv')
print(df.head())

print(df.columns)

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated().sum())

df['Transaction ID'].duplicated().sum()

print(df['Date'].head())

print(df['Date'].dtype)

df['Date']=pd.to_datetime(df['Date'])

df['Year']=df['Date'].dt.year
print(df.info())

df['Month']=df['Date'].dt.month

df['Day']=df['Date'].dt.day

print(df.head())

#KPIs 01
print(df['Total Amount'].sum())

#KPIs 02
list_of_products=df.groupby(['Product Category'])['Total Amount'].sum()
print(list_of_products.index.max())

#KPIs 03
Monthly_sales=df.groupby(['Year','Month'])['Total Amount'].sum()
print(Monthly_sales)

#KPIs 04
print(df['Quantity'].sum())

#KPIs 05
print(df['Total Amount'].mean())
                          
#kPIs 06
list_of_products=df.groupby(['Product Category'])['Total Amount'].sum()
print((list_of_products.index.max()),(list_of_products.values).max())

#KPIs 07
# customer_ages=df.groupby(['Age'])['Total Amount'].sum()
# print((customer_ages.index.max()),(customer_ages.values).max())

ages=pd.cut(df['Age'],bins=[0,20,40,60,80],labels=['0-20','21-40','41-60','61-80'])
age_max=df.groupby(ages)['Total Amount'].sum()
print(age_max.index.max(),age_max.values.max())

#kPIs 08
print(df.groupby(['Gender'])['Total Amount'].sum())

#kPIs 09
print(df.groupby(['Customer ID'])['Total Amount'].sum().sort_values(ascending=False).head(5))

#KPIs 10
print(df.groupby(['Product Category'])['Price per Unit'].mean().sort_values(ascending=False).head(5))

#kPIs 11
monthly_quantity=df.groupby(['Year','Month'])["Quantity"].sum().sort_values(ascending=False).head(5)
print(monthly_quantity)

#kPIs 12
gender_quantity=df.groupby(['Gender'])["Quantity"].sum().sort_values(ascending=False).head(5)
print(gender_quantity)

#kPIs 13
Product_quantity=df.groupby(['Product Category'])["Quantity"].sum().sort_values(ascending=False).head(5)
print(Product_quantity)

#kPIs 14
print(df['Quantity'].mean())

#KPIs 15
print(df['Total Amount'].max())

#KPIs 16
print(df['Total Amount'].min())

#KPIs 17
print(df['Transaction ID'].nunique())

#KPIs 18
print(df['Customer ID'].nunique())

#KPIs 19
amt=df['Total Amount'].sum()
gender_amt=df.groupby(['Gender'])['Total Amount'].sum()
female_amt=gender_amt['Female']
male_amt=gender_amt['Male']
f_percentage=(female_amt/amt)*100
m_percentage=(male_amt/amt)*100
print(f_percentage, m_percentage)

#KPIs 20
cus=df['Customer ID'].nunique()
print(amt/cus)