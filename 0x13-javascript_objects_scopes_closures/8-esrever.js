#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  for (let i = list.length - 1; i >= 0; i--) {
    l[list.length - i - 1] = list[i];
  }
  return (l);
};
