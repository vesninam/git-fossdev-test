import requests 
from datetime import datetime

url_template = "https://simurg.space/gen_file?data=obs&date={date}"
now = datetime.now()
date = now.strftime("%Y-%m-%d")
url = url_template.format(date=date)

response = requests.get(url=url, stream=True)
print(f"For {date} got: ", response)

