#!/usr/bin/node

exports.converter = function (base) {
  return function (nb) {
    if (base === 10) {
      return nb;
    }
    return nb.tostring(base);
  };
};
