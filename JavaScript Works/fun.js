
// In python we use def to reprresent a function here we use function instead of def



// function addnum(n1,n2){
//     return n1+n2
// }

// function addnum(n1,n2,n3){
//     return n1+n2+n3
// }

// console.log(addnum(10,20,30));


// function addnum(...args){
//     let res=0
//     for(let n of args){
//         res+=n
//     }
//     return res
// }

// addnum(10,20)
// addnum(10,20,30)
// addnum(10,20,10,20)

// function cube(num){
//     return num**3
// }

// console.log(cube(3));

// function add(n1,n2){
//     return n1=n2
// }
// console.log(add(10,20));

// var cube=(n)=>n**3

// var maxtwo=(n1,n2)=>n1>n2?n1:n2

// var numchk=(num)=>num>0?'+ve':num<0?'-ve':'zero'
// console.log(numchk(1));

var smartsub=(n1,n2)=>n1>n2?n1-n2:n2-n1
console.log(smartsub(30,10));