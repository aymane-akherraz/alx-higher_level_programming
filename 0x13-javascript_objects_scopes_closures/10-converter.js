#!/usr/bin/node

exports.converter = function (base) {
  return function (nb) {
    if (base === 10) {
      return nb.toString();
    }
    return nb.toString(base);
  };
};
