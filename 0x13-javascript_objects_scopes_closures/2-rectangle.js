#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' &&
        Number.isInteger(w) && Number.isInteger(h) &&
        w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
