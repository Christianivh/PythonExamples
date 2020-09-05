import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

df_covid19 = pd.read_json('http://pomber.github.io/covid19/timeseries.json')
df_covid19.head()

import datetime as dt

country_all = df_covid19.columns

df_all = pd.DataFrame({dt.datetime:None, int:None, int:None, object:None},
                        columns = ['date','confirmed','deaths','recovered', 'country'])

for country in country_all[1:]:
  df_country = pd.json_normalize(df_covid19[str(country)])
  df_country['country'] = country
  df_all = df_all.append(df_country, ignore_index = True)

df_all['date'] = pd.to_datetime(df_all['date'] , infer_datetime_format=True)

df_all.to_csv("covid19.csv", index=False)

print("total de registros:", len(df_all))
print("Ultima fecha cargada:", max(df_all['date']))
