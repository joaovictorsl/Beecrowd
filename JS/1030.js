const { LinkedList } = require('./utils/LinkedList.js');

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let cases = Number(lines[0]);

function josephus(peopleArray, step) {
  if (peopleArray.length === 1) {
    return peopleArray.getFirst();
  }
  let toRemove;
  for (let i = 0; i < step - 1; i++) {
    toRemove = peopleArray.next();
  }
  peopleArray.remove(toRemove);
  return josephus(peopleArray, step);
}

for (let i = 1; i <= cases; i++) {
  let [people, step] = lines[i].split(' ').map(v => Number(v));
  let peopleArray = [];
  for (let i = 1; i <= people; i++) {
    peopleArray.push(i);
  }
  peopleArray = new LinkedList(peopleArray);
  let survivor = josephus(peopleArray, step).value;
  console.log(`Case ${i}: ${survivor}`);
}
