// ********************* Inheritance between Class ***************************

// Inheritance between class

// Child inherits Parent class we write " child extends parent "


class Parent{
    m1(){
        console.log("inside m1");
    }
}

class Child extends Parent {

}

var c=new Child()
c.m1()


// Not support method overloading

// class Operations{
//     add(n1,n2){
//         return n1+n2
//     }
//     add(n1,n2,n3){
//         return n1+n2+n3
//     }
//     add(n1,n2,n3,n4){
//         return n1+n2+n3+n4
//     }
// }


class Operations{
    add(...args){
        return args.reduce((n1,n2)=>n1+n2)
    }
}

var add=new Operations()
console.log(add.add(1,2,3,4,5));