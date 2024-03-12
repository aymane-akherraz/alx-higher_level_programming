#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rect = '';
        for (let j = 0; j < this.width; j++) {
          rect += c;
        }
        console.log(rect);
      }
    }
  }
}
module.exports = Square;
