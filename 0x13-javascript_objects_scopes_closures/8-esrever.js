#!/usr/bin/node
exports.esrever = function (list) {
    const newList = [];
    for (let count = list.length - 1; count >= 0 ; count--) {
        newList.push(list[count]);
    }
    return newList;
}