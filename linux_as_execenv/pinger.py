import requests 

url_template = "https://simurg.space/gen_file?data=obs&date={date}"
date = "2026-02-19"
url = url_template.format(date=date)

response = requests.get(url=url, stream=True)
print(f"For {date} got: ", response)

