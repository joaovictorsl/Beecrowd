class LinkedList {
  constructor(baseArray) {
    this.first = new Node(baseArray[0]);
    let second = new Node(baseArray[1], this.first, this.first);
    this.first.next = second;
    let prev = second;
    for (let i = 2; i < baseArray.length; i++) {
      let addedNode = new Node(baseArray[i], prev, this.first);
      prev.next = addedNode;
      prev = addedNode;
    }
    this.first.prev = prev;
    this.iterator = this.first;
    this.length = baseArray.length;
  }

  getFirst() {
    return this.first;
  }

  next() {
    this.iterator = this.iterator.next;
    return this.iterator;
  }

  getIterator() {
    return this.iterator;
  }

  prev() {
    this.iterator = this.iterator.prev;
    return this.iterator;
  }

  remove(nodeToRemove) {
    if (nodeToRemove === this.first) {
      this.first = nodeToRemove.next;
    }
    let prev = nodeToRemove.prev;
    let next = nodeToRemove.next;
    prev.next = next;
    next.prev = prev;
    this.length--;
    this.iterator = next;
  }
}

class Node {
  constructor(value, prev, next) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }
}

module.exports = { LinkedList }
