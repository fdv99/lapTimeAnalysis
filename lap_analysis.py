import pandas as pd
f=pd.read_csv("23_Time Cards_Race.csv", sep=';', skipinitialspace=True)
keep_col = ['NUMBER', 'LAPNUMBER', 'LAPTIME', 'TOP_SPEED', 'DRIVER_NAME', 'CLASS']
new_f = f[keep_col]
new_f.to_csv("daytona_2019_fv.csv", index=False)