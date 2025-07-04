{/* <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p> */}
// A palindromic number　回文数
//9009 91*99


function palinfromicNum(){
    let maxNum = -Infinity;
    
    for(let i=999; i>=100; i--){
        for(let j=999; j>=100; j--){
            number = i * j
            str = number.toString();
            str1 = str.split('').reverse().join('');
            if(str == str1 ){
                if(number > maxNum){
                    maxNum = number;
                    a = i;
                    b = j;
                }
            }
        }
    
    }
    return result = [{
            number:maxNum,
            factor1:a,
            factor2:b,
        }];;
}

console.log(palinfromicNum())