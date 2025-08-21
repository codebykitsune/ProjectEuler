{/* <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p> */}

function PrimeFactors(n){
    let list =[]
    let i = 2
    while (i * i <=n){
        while (n % i == 0){
            list.push(i);
            n = n / i;
        }
        i++;
    }

    if(n >1){
        list.push(n);
    }
    return compareElements(list);
}

//sort
function compareElements(list){
    let maxNum = -Infinity;
    for(i=0; i<list.length; i++){
        if(list[i]>maxNum){
            maxNum = list[i]
        }
    }
    return maxNum

}

//console.log(PrimeFactors(13195))
console.log(PrimeFactors(600851475143))