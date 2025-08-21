//三角数を求める→わかる
//求めた数の約数を求める→わからない
//
//三角数
function HighlyDivisibleTriangularNumber(){
    let i=2;
    while(i>0){
        //三角数を求める→わかる
        triangularNum = i*(i+1)/2;
        divisors = countDivisors(triangularNum);
        if(divisors>=500){
            return  triangularNum;
        }
        i++
    }
}
console.log(HighlyDivisibleTriangularNumber())

//求めた数の約数を求める→関数化
function getPrimeFactors(n){
    const factors = {};
    let i=2;
    while (i * i <=n){
        let count =0
        while (n % i == 0){
            count++
            n = n / i;
        }
        if (count > 0) {
            factors[i] = count;
          }
        i++;
    }
    if (n > 1) {
        factors[n] = 1;
      }
    return factors
}

function countDivisors(n){
    const elements = getPrimeFactors(n);
    let count = 1;
    for (exponentiation of Object.values(elements)){
        count *= (exponentiation +1)
    }
    return count

}
//console.log(countDivisors(60));