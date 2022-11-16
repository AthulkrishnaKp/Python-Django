

// Pallindrom of a number

// Coercion in Javascript important property

var num=121
var n=num


var res=''
while(num!=0){
    let lastdigit=num%10
    res+=lastdigit
    // console.log(lastdigit);
    num=Math.floor(num/10)
}
console.log(n==res?"palindrom":"not palindrom");