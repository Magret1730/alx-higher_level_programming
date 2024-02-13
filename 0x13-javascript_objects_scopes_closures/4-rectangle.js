#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Object.create(Rectangle);
    } else if (w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const exchange = this.width;
    this.width = this.height;
    this.height = exchange;

    return this;
  }

  double () {
    this.width *= 2;
    this.height *= 2;

    return this;
  }
}

module.exports = Rectangle;
