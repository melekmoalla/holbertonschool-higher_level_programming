#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
    const counts = {};
    for (const num of list) {
        counts[num] = counts[num] ? counts[num] + 1 : 1;
      }
    return counts[searchElement]
}