function test(){
    let list =[];
    let maxNum = -Infinity;
    let j = 0
    for(i=1000000; i>1; i--){
        Num = CollatzSequence(i);
        if(Num >maxNum){
            maxNum = Num;
            maxI = i;
        }
    }
    return maxI;
}

function CollatzSequence(n){
    let list =[]
    while(n>1){
        if(n%2 ==0){
            n = n / 2;
            list.push(n);
        }else{
            n = n * 3 +1;
            list.push(n);
        }
    }
    return list.length;
}
console.log(test())