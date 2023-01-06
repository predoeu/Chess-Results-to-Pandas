import pandas as pd
def cr_to_pandas(tnr):

    link = 'http://chess-results.com/tnr{}.aspx?lan=1&zeilen=0&art=1&rd=5&prt=4&excel=2010'.format(tnr)
    
    df = pd.read_excel(link)
    start = (df[df['From the Tournament-Database of Chess-Results http://chess-results.com']=='Rk.'].index.values) + 1
    start = int(start)
    end = (df[df['From the Tournament-Database of Chess-Results http://chess-results.com']=='Annotation'].index.values) - 1
    end = int(len(df) - end)
    df = pd.read_excel(link, skiprows=inicio, skipfooter=fim)
    return df