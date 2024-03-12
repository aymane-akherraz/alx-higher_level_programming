class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' &&
        Number.isInteger(w) && Number.isInteger(h) &&
        w > 1 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
