for(let i=1;i<=10;i+=2){
    console.log(`${i} * 4 = ${i*4}`)
}

/*
function factorial(n) {
  let result = 1;

  for (let i = 1; i <= n; i+=1) {
    result *= i;
  }

  return result;
}

console.log(factorial(5))*/

let fact=1
for(let i=1;i<=5;i++){
    fact*=i
}
console.log(`Factorial of 5 is ${fact}`)


let num=5
let i=1
let result=1

while(i<=num){
    result*=i
    i++
}
console.log(result)