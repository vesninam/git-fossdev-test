import requests 
from datetime import datetime, timedelta

url_template = "https://simurg.space/gen_file?data=obs&date={date}"
current = datetime.now()

while True:
    date = current.strftime("%Y-%m-%d")
    url = url_template.format(date=date)

    response = requests.get(url=url, stream=True)
    print(f"For {date} got: ", response)
    if response.status_code == 200:
       print(f"Last available data are for {date}")
       break
    else:
       current = current - timedelta(days=1)

