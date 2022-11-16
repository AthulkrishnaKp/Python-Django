
// create object person
// var person={
//     name:"Athul",
//     age:23,
//     gender:"male"
// }

// console.log(person.name,person.age,person.gender);

// creating attribute to person object
// person.salary=4000;
// console.log(person);
// output = { name: 'Athul', age: 23, gender: 'male', salary: 4000 }

// check wheather a key is in person 
// console.log("isActive" in person);    //  returns false
// console.log("name" in person);        //  returns true


// Function can be written within objects like down :

var person={
    name:"Athul",
    age:23,
    gender:"male",
    getName(){
        return this.name
    },
    getAge(){
        return this.age
    }
}

console.log(person.getName());
console.log(person.getAge());

