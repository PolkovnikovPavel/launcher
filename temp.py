import requests

options = requests.get('https://raw.githubusercontent.com/PolkovnikovPavel/launcher/master/options').text

with open('version.txt', encoding='utf-8') as f:
    version, name = f.read().split(':')
new_version = options.split('\n')[0]

if version != new_version:
    for data in options.split('\n')[1::]:
        v, url = data.split(' - ')
        if v == new_version:
            r = requests.get(url)
            with open(name, 'wb') as f:
                f.write(r.content)
            with open('version.txt', 'w', encoding='utf-8') as f:
                f.write(f'{new_version}:{name}')
            print('Обновление прошло успешно')
            break
elif version == new_version:
    print('Уже установлена последняя версия')

