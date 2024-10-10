import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Nassau&$limit=50000'

##using low_memory parameter to false when importing allows pandas more memory to process the data
##this help fixed the issue when i specified to use certain columns 

df= pd.read_csv(url, low_memory=False)
print(df.columns)

## specify columns
df = pd.read_csv(url, usecols=['race','ethnicity','age_group', 'gender', 'length_of_stay', 'total_charges', 'total_costs', 'type_of_admission'])
print(df)

## convert data to numeric or else it only display count, unique, top and freq
## errors ='coerce' will turn any non-numeric values to NaN
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')

## use describe methode to summarize data
print(df[['length_of_stay', 'total_charges', 'total_costs']].describe())

## count distribution and bar plots
age_count = df['age_group'].value_counts()
print(age_count)
ax = age_count.plot.bar(rot=0, title='Age Group Distribution')
ax.set_ylabel('Count')
plt.show()

sex_count = df['gender'].value_counts()
print(sex_count)
sx = sex_count.plot.bar(rot=0, title = 'Sex Count')
sx.set_ylabel('Count')
plt.show()

adm_typ = df['type_of_admission']
print(adm_typ)
admx = adm_typ.plot.bar(rot=0, title = 'Type of Admission')
admx.set_ylabel('Count')
plt.show()

## histogram

len_stay = df['length_of_stay'].value_counts()
print(len_stay)
lx = len_stay.plot.hist(stacked=True)
plt.show()

## boxplot

tot_chrgs = df ['total_charges'].describe()
print(tot_chrgs)
tx = tot_chrgs.plot.box()
plt.show()

## handle missing data

missing_data = df.isnull().sum()
print(missing_data)

## Ethnicity and Race

print(df.head())

eth_grp = df.groupby('ethnicity')[['total_charges', 'length_of_stay']].mean()
rce_grp = df.groupby('race')[['total_charges', 'length_of_stay']].mean()

print("Ethnicity Group Analysis:\n", eth_grp)
print("\nRace Group Analysis:\n", rce_grp)

plt.figure(figsize=(10, 8))
correlation_matrix = df[['total_charges', 'length_of_stay']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

