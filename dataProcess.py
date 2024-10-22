import pandas as pd
import numpy as np


df = pd.read_csv("MBA.csv").drop(["application_id"], axis=1)
print(df)

# drop waitlisted (to make admission binary)
for index, row in df.iterrows():
    if row['admission'] == "Waitlist":
        df = df.drop(index, axis=0)

df = df.reset_index().drop("index", axis=1)

# admission to 0/1
df.loc[pd.isna(df['admission']), 'admission'] = 0
df.loc[df['admission'] == "Admit", 'admission'] = 1

df.loc[df['international'] == "False", 'international'] = 0
df.loc[df['international'] == "True", 'international'] = 0

df['international'] = df['international'].astype(int)
df['admission'] = df['admission'].astype(int)

for num in ['gpa', 'gmat', 'work_exp']:
    df[num] = df[num]/(max(list(df[num])))

df['race'], uniques = pd.factorize(df['race'])
df['gender'], uniques = pd.factorize(df['gender'])
df['major'], uniques = pd.factorize(df['major'])
df['work_industry'], uniques = pd.factorize(df['work_industry'])

df = pd.get_dummies(df, columns=['major', 'race', 'work_industry'])

df.to_csv("processed_data.csv")
print(df)
