import pandas as pd

def uno():
    data = {'a': [100,150], 'b': [200,250], 'c': [300,350], 'd': [400,350], 'e': [800,850]}
    print (pd.Series(data))

def dos():
    data =[[2, 3, 4], [5, 6, 7]]
    print (pd.Series(data))

def tres():
    data = {'a': [100,150], 'b': [200,250], 'c': [300,350], 'd': [400,350], 'e': [800,850]}
    df = pd.DataFrame(data)
    print (df)
    cuatro(df)

def cuatro(df):
    df2 = pd.DataFrame({'a': [175], 'b': [275], 'c': [375], 'd': [475], 'e': [875]})
    df = df.append(df2, ignore_index = True)
    print (df)
    cinco(df)

def cinco(df):
    df.to_csv('CwHwDomene.csv', index = False)

def seis():
        return pd.read_csv('pokemon.csv')

def siete(df):
    print (df[:5])

def ocho(df):
    print (df[-5:])

def nueve(df):
    df.set_index('Name', inplace = True)
    
def diez(df):
    print (df.iloc[6])

def once(df):
    print (df.loc['Mew'])

def doce(df):
    is_ghost = df['Type 1'] == 'Ghost'
    print (df[is_ghost])

def trece(df):
    is_speed = df['Speed'] > 120
    print (df[is_speed])

def catorce(df):
    is_legend = df['Legendary']
    print (df[is_legend].filter(items = ['Type 1', 'Type 2']))

uno()
dos()
tres()
pk = seis()
siete(pk)
ocho(pk)
nueve(pk)
diez(pk)
once(pk)
doce(pk)
trece(pk)
catorce(pk)
