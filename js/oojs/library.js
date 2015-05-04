//decorator pattern
var carlike = function(obj, loc){
	obj.loc = loc;
	obj.move = function(){
		obj.loc++;
	};
};

var Car = function(loc){
	var obj = {loc:loc};
	obj.loc = loc;
	obj.move = function(){
		obj.loc++;
	};
};

var Van = function(loc){
	var obj = Car(loc);
	obj.grab = function(){/*...*/};
	return obj;
};

//prototypal
// create object that delegates from car,prototype
var Car = function(loc){
	var obj = Object.create(Car.prototype);
	obj.loc = loc;
	return obj;
};

Car.prototype.move  = function(){
		this.loc++;
};

var Van = function(loc){
	Car.call(this, loc);
};
Van.prototype = Object.create(Car.prototype);
Van.prototype.constructor = Van;
Van.prototype.grab = function(){/*...*/};