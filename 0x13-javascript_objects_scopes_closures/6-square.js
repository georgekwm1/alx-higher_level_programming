const Square5 = require('./5-square.js');

class Square extends Square5 {
    constructor(size) {
        super(size, size);
    }

    charPrint(c) {
        if (c === undefined)
            this.print();
        else {
            for (let count = 0; count < this.height; count++) {
                console.log(`${c}`.repeat(this.width));
            }
        }
    }
}

module.exports = Square;
