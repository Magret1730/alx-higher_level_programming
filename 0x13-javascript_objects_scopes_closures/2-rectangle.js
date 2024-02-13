#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // Object.create(Rectangle);
      new Rectangle();
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
