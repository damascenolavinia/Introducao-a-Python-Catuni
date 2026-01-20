import pandas as pd 
dataset_lavinia_damasceno = 'dataset_lavinia_damasceno.csv'
df = pd.read_csv(dataset_lavinia_damasceno, sep=',')
print(df.head())