#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (isNaN(h) || isNaN(w) || h <= 0 || w <= 0) {
      // Empty object
    } else {
      this.w = w;
      this.h = h;
    }
  }

  print () {
    for (let i = 0; i < this.h; i++) {
      for (let a = 0; a < this.w; a++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
