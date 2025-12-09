import os
import pandas as pd
import matplotlib.pyplot as plt

### open the csv file
os.chdir(os.path.dirname(__file__))
df= pd.read_csv("Banking.csv")
print(df)

### pie chart
plt.subplot(2,2,1)
Nationality_counts = df['Nationality'].value_counts()
plt.pie(Nationality_counts.values, labels=Nationality_counts.index)
plt.legend(title='NATIONALITY')
plt.title('DISTRIBUTION OF BANK CUSTOMERS BY NATIONALITY')

### bar chart
plt.subplot(2,2,2)
Nationality_loans = df.groupby('Nationality')['Bank Loans'].mean()
colors= ['green','blue','red','purple','cyan']
plt.bar(Nationality_loans.index, Nationality_loans.values, color=colors)
plt.title('RELATION BETWEEN BANK LOANS AND NATIONALITY')
plt.xlabel('Nationality')
plt.ylabel('BANK LOANS')
plt.ylim(500000,650000)

### line chart
plt.subplot(2,2,3)  
age_loans= df.groupby('Age')['Bank Loans'].mean()
plt.plot(age_loans.index, age_loans.values, marker='o')
plt.title('RELATIONSHIP BETWEEN AGE AND LOANS')
plt.xlabel('AGE')
plt.ylabel('LOANS')

### histogram
plt.subplot(2,2,4)
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('AGE DISTRIBUTION')
plt.xlabel('Age')
plt.ylabel('Frequency')

### show the charts
plt.tight_layout() 
plt.show()