
function Square(A, B, C, D) {
  this.a = A;
  this.b = B;
  this.c = C;
  this.d = D;
}

Square.prototype.isSquare = function() {
  if ((this.a === this.b) && (this.b === this.c) && (this.c === this.d)){
  console.log(true)
  }
  else {
  console.log(false)
  }
};

var obj_square = new Square(10,10,10,10);
var bool_value = obj_square.isSquare();

