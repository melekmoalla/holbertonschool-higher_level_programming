#!/usr/bin/node
class Rectangle {
  constructor (weight, height) {
    if (isNaN(height) || isNaN(weight) || height <= 0 || weight <= 0) {
      // Empty object
    } else {
      this.width = weight;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let a = 0; a < this.width; a++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
