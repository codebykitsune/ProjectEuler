{/* <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
<p>Find the sum of all the primes below two million.</p> */}

function SummationOfPrimes(limit) {
    // 1. 最初は、すべての数を「素数」だと思う（true）
    let isPrime = new Array(limit).fill(true);
    
    // 0と1は素数ではないから false にする
    isPrime[0] = false;
    isPrime[1] = false;

    // 2からスタートして、素数じゃないものを消す
    for (let i = 2; i * i < limit; i++) {
        // もしiが素数なら（まだtrueのままなら）
        if (isPrime[i]) {
            // iの倍数は素数じゃないから false にする
            for (let j = i * i; j < limit; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // 2. 残ったtrueの場所だけ合計する
    let sum = 0;
    for (let i = 2; i < limit; i++) {
        if (isPrime[i]) {
            sum += i;
        }
    }

    return sum;
}

// 実行してみる
console.log(SummationOfPrimes(2000000));
