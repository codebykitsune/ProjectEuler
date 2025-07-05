//1,2,3,4,5,6,7,8,9,10
//2**3,3**2,5,7 2520
//Euclidean Algorithm
//LCM関数を用いる

function SmallestMultiple(n){
    let list = [];
    let result = 1;
    for(i=2; i<n; i++){
        result = LCM(result,i);
    }
    return result;
}
console.log(SmallestMultiple(20))

//Euclidean Algorithm
function GCD(a,b){
    while(b !==0){
        let q = b;
        b = a % b;
        a = q;
    }
    return a;
};

function LCM(a,b){
    return a*b/GCD(a,b)
}
