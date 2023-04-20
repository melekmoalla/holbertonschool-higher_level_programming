#!/usr/bin/node
exports.esrever = function (list) {
  const reversedArray = [];

  for (let i = list.length - 1; i >= 0; i--) {
    const valueAtIndex = list[i];

    reversedArray.push(valueAtIndex);
  }

  return reversedArray;
};
