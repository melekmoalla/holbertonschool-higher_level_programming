#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
    const counts = {};
    for (const num of list) {
        counts[num] = counts[num] ? counts[num] + 1 : 1;
      }
    if (counts[searchElement] === undefined){
        return 0
    }
    return counts[searchElement]
}