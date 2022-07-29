#!/usr/bin/node
exports.addMeMaybe = function (number, func) {
  number++;
  func(number);
};
