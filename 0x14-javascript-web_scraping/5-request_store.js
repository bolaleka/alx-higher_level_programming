#!/usr/bin/node
// vim: set ts=2 sw=2 sts=2 et:
'use strict';

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`HTTP ${response.statusCode}: ${response.statusMessage}`);
    process.exit(1);
  }

  fs.writeFile(filepath, body, { encoding: 'utf-8' }, function (error) {
    if (error) {
      console.error(error);
      process.exit(1);
    }
  });
});
