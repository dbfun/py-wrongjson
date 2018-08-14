"use strict";

/*
Простой скрипт, эксплуатирующий пакет dirty-json
  на вход stdin: не валидный JSON
  получаем в stdout: валидный JSON
*/

const
  fs = require('fs'),
  dJSON = require('dirty-json'),
  stdinBuffer = fs.readFileSync(0) // STDIN_FILENO = 0
  ;

const wrongJSON = dJSON.parse(stdinBuffer.toString());
process.stdout.write(JSON.stringify(wrongJSON));
