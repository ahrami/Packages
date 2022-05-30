import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(1) #1
df = pd.read_csv('anime.csv', thousands=',', na_values=['?', '-'], parse_dates = ['Airdate'])
df['Airdate'] = df['Airdate'].str.replace(' (JST)', '-0900')
df['Airdate'] = pd.to_datetime(df['Airdate'], errors='coerce')

print(2) #2
print("First 10 rows:")
print(df.head(10))

print(3) #3
print("Info:")
for column in df.columns:
    print(column, ': ', df[column].dtypes, sep = '')
    
print(4) #4
df.rename(columns=str.lower, inplace=True)
for column in df.columns:
    print(column)
df['title'] = df['title'].astype('string')
for i in range(0, df['title'].size):
    df['title'][i] = df['title'][i].replace(' ', '_')

print(5) #5
for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        print(column, ':', sep = '')
        print(df[column].describe())

print(6) #6
for column in df.columns:
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(column, ':', sep = '')
        print(df[column].value_counts())

print(8) #8
#8a
fig = plt.figure('Production')
pr = df['production'].value_counts()[:30]
#pr = df['production'].value_counts()
pr.plot.barh()
#8b
fig = plt.figure('Episodes')
ep = df['episodes'].value_counts()[:30]
#ep = df['episodes'].value_counts()
ep.plot.barh()
#8c
fig = plt.figure('Source')
sr = df['source'].value_counts()[:30]
#sr = df['source'].value_counts()
sr.plot.barh()
#8d
fig = plt.figure('Theme')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['theme'].str.contains(theme, na=False, regex=False).sum()    
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)
#8e
fig = plt.figure('Year')
yr = df['airdate'].groupby(df['airdate'].dt.year).count()
yr.plot()

print(9) #9
fig = plt.figure('Rating')
rmean = df['rating'].groupby(df['production']).mean()
rmean = rmean.sort_values(ascending = False)[:30]
#rmean = rmean.sort_values(ascending = False)
rmean.plot.barh()

print(10) #10
fig = plt.figure('Rating Intervals')
rt = df['rating'].groupby(by=(df['rating'].apply(np.floor)), dropna=True).count()
rt.plot.barh()

print(11) #11

fig = plt.figure('Cool Themes Where Rating > 8')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['theme'].str.contains(theme, na=False, regex=False).where(df['rating'] > 8).sum()    
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Cool Genres Where Rating > 8')
masked = set(df['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['genre'].str.contains(theme, na=False, regex=False).where(df['rating'] > 8).sum()    
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Themes Rating Average')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['rating'].where(df['theme'].str.contains(theme, na=False, regex=False)).mean() 
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Genres Rating Average')
masked = set(df['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['rating'].where(df['genre'].str.contains(theme, na=False, regex=False)).mean() 
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

print(12) #12
fig = plt.figure('Voters Rating')
x = list(df['voters'])
y = list(df['rating'])
plt.plot(x, y)

print(13) #13
fig = plt.figure('Themes Voters')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['voters'].where(df['theme'].str.contains(theme, na=False, regex=False)).mean() 
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Genres Voters')
masked = set(df['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['voters'].where(df['genre'].str.contains(theme, na=False, regex=False)).mean() 
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

plt.show()
