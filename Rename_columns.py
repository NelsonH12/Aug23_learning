import pandas as pd
df_premier24 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv") 
#press copy link address on the desired link
#changing column names
df_premier24.rename(columns={"Time" : "Fun","Div" : "Me"}, inplace=True)
print(df_premier24)