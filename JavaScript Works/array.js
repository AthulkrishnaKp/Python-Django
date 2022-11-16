// Array

//  methods in array : Map,filter,reduce,find,some,sort,forEach,includes => IMPORTANT




// ************************************************************************
// Sorting

// var arr=[10,2,9,3,4,5]

// console.log(arr.length);

// for (let n of arr){
//     if(n%2!=0)
//         console.log(n);
// }

// arr.sort((o1,o2)=>o1<o2?-1:1)

// arr.sort((o1,o2)=>o2-o1)
// console.log(arr);

// ************************************************************************
 
// Mapping map and Filter :

// var arr=[10,2,9,3,4,5]

// arr.map(n=>n**2).filter(n=>n>50).forEach(n=>console.log(n))

// var cubes=arr.map(n=>n**2)
// console.log(cubes);

// var odd=arr.filter(n=>n%2 !=0)
// console.log(odd);

// If number<5 print num-1 and if number>5 print num+1

// var lst=[1,2,3,4,6,7,8,12,13]

// var list=lst.map(n=>n<5?n-1:n+1)
// console.log(list);

// *************************************************************************

//  Reduce Function( sort and reduce will have only two arguments in function)

// var arr=[10,2,9,3,4,5,15]

// sum of all elements :
// var sum=arr.reduce((n1,n2)=>n1+n2)
// console.log(sum);

// Products of array :
// var sum=arr.reduce((n1,n2)=>n1*n2)
// console.log(sum);

// Max of an array elements :
// var max=arr.reduce((n1,n2)=>n1>n2?n1:n2)
// console.log(max);

// ***************************************************************************

//  For Each function :

// var arr=[10,2,9,3,4,5,15]

// arr.forEach(n=>console.log(n))

// ***************************************************************************

// Some function :

// is Testing available result is a bolean value ie True or False then we use some:

// continue in courses page: