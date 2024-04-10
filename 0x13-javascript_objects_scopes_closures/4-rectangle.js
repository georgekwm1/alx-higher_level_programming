class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
            return undefined;
        }
        else {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        for (let count = 0; count <this.height; count++) {
            console.log("X".repeat(this.width));
        }
    }
    double() {
        this.width *= 2;
        this.print();
        return this.print;
    }
    rotate() {
        let new_width = this.height;
        this.height = this.width/2;
        this.width = new_width;
        this.double();
        return this;
    }
}

module.exports = Rectangle;