// The sum of the squares of the first ten natural numbers is,</p>
// $$1^2 + 2^2 + ... + 10^2 = 385.$$
// <p>The square of the sum of the first ten natural numbers is,</p>
// $$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
// <p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
// <p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>

function SumSquareDifference(n){
    let sum1 = 0
    let sum2 = 0
    for(i=1; i<=n; i++){
        sum1 += i**2
        sum2 += i 
    }
    sum2 = sum2**2
    return sum2 - sum1;
}
console.log(SumSquareDifference(100))