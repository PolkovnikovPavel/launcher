import requests


session = requests.Session()
r = session.get('https://github.com/PolkovnikovPavel/collection_lfk/raw/master/old_version/%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB%20%D0%BB%D1%84%D0%BA%20v-1.7.exe')
print(r.content)


