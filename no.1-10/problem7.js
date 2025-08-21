{/* <p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
<p>What is the $10\,001$st prime number?</p> */}
//2, 3, 5, 7, 11, 13
//13 is 6th

function PrimeNumber(n){
    index=0;
    number=2;
    result = 0;

    while(index<n){
        if(isPrime(number)){
            index+=1
            result = number
        }
        number+=1
    }
    return result;
  }

console.log(PrimeNumber(10001))

//whether is Prime number or not
function isPrime(n){
    if(n<2){
        return false;
    }
    for(i=2; i<=Math.sqrt(n); i++){
        if(n%i === 0){
            return false;
        }

    }
    return true;
}