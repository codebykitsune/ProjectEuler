// If we list all the natural numbers below 10 that are multiples of 3 or 5, 
// we get 3,5,6 and 9.
// The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.


//[3,5,6,9] 23
//sum[3,5,6,9,10,12,15]
function Problem01(a,b){
    let count = 0;
    for (i=0; i<1000; i++){
      if(i%a == 0 || i%b == 0){
          count += i
      }
    }
    return count;
  }
  
console.log(Problem01(3,5))
  
