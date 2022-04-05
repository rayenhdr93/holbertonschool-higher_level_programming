#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let txt = '';
      for (let i = 0; i < this.width; i++) {
        txt += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(txt);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
