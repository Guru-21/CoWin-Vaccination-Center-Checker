import requests
from fake_useragent import UserAgent
import pandas as pd


ua = UserAgent()
header = {'User-Agent': str(ua.chrome)}
pin = '713340'
date = '21-05-2021'
response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin}&date={date}",headers=header)
data = response.json()
print(data)


centers = pd.DataFrame(data.get('centers'))

if centers.empty:
    print("DataFrame is Empty")

session_ids=[]
for j, row in centers.iterrows():
    session = pd.DataFrame(row['sessions'][0])
    session['center_id'] = centers.loc[j, 'center_id']
    session_ids.append(session)

sessions = pd.concat(session_ids, ignore_index= True)
av_centeres = centers.merge(sessions,on = 'center_id')
av_centeres.drop(columns=['sessions','session_id','lat','block_name','long','from','to'],inplace=True)
print(av_centeres)
#av_centeres.to_csv("test.csv")   # csv file
#print(av_centeres.columns)
#av_centeres = av_centeres[av_centeres['min_age_limit']==18]
#print(av_centeres)
#av_centeres.to_csv('test.csv')















