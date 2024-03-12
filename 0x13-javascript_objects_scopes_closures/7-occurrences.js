#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let nb = 0;
  let i = 0;
  while (i < len) {
    if (list[i] === searchElement) {
      nb++;
    }
    i++;
  }
  return nb;
};
