#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destFile = process.argv[4];

const data = fs.readFileSync(fileA, 'utf8');
const data1 = fs.readFileSync(fileB, 'utf8');

const data2 = data + data1;

fs.writeFileSync(destFile, data2);
