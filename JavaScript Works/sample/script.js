
//  Addition

// Both add and substract :

function add(e){
    console.log(e.target.value);
    let op=e.target.value
    let n1=id_num1.value
    let n2=id_num2.value
    let result=0
    if(op=="+"){
        result=Number(n1)+Number(n2)
    }
    else if(op=="-"){
        result=Number(n1)-Number(n2)
    }
    document.querySelector("#id_result").innerHTML=`
    <div class="alert alert-success" role="alert">
  result=${result}
</div>
    `
}





//  Substraction

// function substract(){
//     let n1=id_num1.value
//     let n2=id_num2.value
//     let result=Number(n1)-Number(n2)
//     document.querySelector("#id_result").innerHTML=`
//     <div class="alert alert-success" role="alert">
//   result=${result}
// </div>
//     `
// }


// function add(e){
//     // let n1=document.querySelector("#id_num1").value
//     // let n2=document.querySelector("#id_num2").value
//     console.log(e.target.value);
//     let op=e.target.value
//     let n1=id_num1.value
//     let n2=id_num2.value
//     // let result=Number(n1)+Number(n2)
//     let result=0
//     if(op=="+"){
//         result=Number(n1)+Number(n2)
//     }
//     else if(op=="-"){
//         result=Number(n1)-Number(n2)
//     }
//     document.querySelector("#id_result").innerHTML=`
//     <div class="alert alert-success" role="alert">
//   result=${result}
// </div>
//     `
// }