import requests
r = requests.get('')
# сразу распаршено!
res = r.content
print(res)