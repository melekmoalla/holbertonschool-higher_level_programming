#!/usr/bin/node
const Rectangle = class {
  constructor (height, width) {
    if (isNaN(height) || isNaN(width) || height <= 0 || width <= 0) {
      // Empty object
    } else {
      this.width = width;
      this.height = height;
    }
  }
};
module.exports = Rectangle;
