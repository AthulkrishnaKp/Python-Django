

// inheritance between objects
// object_name.__proto__=parent_object_name

var baleno={
    varient:"petrol",
    name:"baleno",
    price:"9lakhs",
    color:["red","black"],
    break:"abs",
    brand:"nexa",
    getPrice(){
    return this.price
    }
}

var glanza={
    name:"glanza",
    brand:"toyota",
    price:"10lakhs"
}

glanza.__proto__=baleno
console.log(glanza.break);
console.log(glanza);

