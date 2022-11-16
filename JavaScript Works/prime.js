

// Check prime numbers

var num=11


var isPrime=true
for(let i=2;i<num;i++){
    if(num%i==0){
        isPrime=false
        break
    }
}
console.log(`is ${num} prime = ${isPrime}`);