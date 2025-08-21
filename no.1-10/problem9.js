{/* <p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p> */}



//a+b+c = 1000

function SpecialPythagoreanTriplet(sum){
    let list =[]
    // a**2 + b**2 === c**2
    //先にa + b + c = 1000を探す
    for(a=1; a<sum; a++){
        for(b=sum; b>0; b--){
            let c = sum - a - b;
            if(a**2 + b**2 == c**2 && a<b){
                list.push(a)
                list.push(b)
                list.push(c)
                return list
                
            }
        }
    }

}
console.log(SpecialPythagoreanTriplet(1000));