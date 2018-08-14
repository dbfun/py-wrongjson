# -*- coding: utf-8 -*-
import json
from subprocess import Popen, PIPE

# Наш невалидный JSON
a = '{"geo":"Москва","name":"МГТУ "Станкин" (Московский государственный технологический университет Станкин)","faculty_id":"1130078"}'

# Обработка через NodeJS
process = Popen(["node", "dirty-json.js"], stdin=PIPE, stdout=PIPE)

# Пишем в stdin
process.stdin.write(a)

# Получаем из stdout
(output, err) = process.communicate()

# Код завершения
exit_code = process.wait()

# Парсим исправленный JSON
b = json.loads(output)
print b
