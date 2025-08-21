//多倍長整数演算に関するJSのコード
//This is JS code about Arbitrary-precision arithmetic
//参考資料 https://qiita.com/square1001/items/1aa12e04934b6e749962
//大きすぎる数を配列の形にする
//N 桁の数を、長さ N の配列として管理する
//example:16777216
//digit = { 6, 1, 2, 7, 7, 7, 6, 1 }
//一の位から始める
// vector<int> addition(vector<int> digit_a, vector<int> digit_b) {
// 	int N = max(digit_a.size(), digit_b.size()); // a と b の大きい方
// 	vector<int> digit_ans(N); // 長さ N の配列 digit_ans を作る
// 	for(int i = 0; i < N; ++i) {
// 		digit_ans[i] = (i < digit_a.size() ? digit_a[i] : 0) + (i < digit_b.size() ? digit_b[i] : 0);
// 		// digit_ans[i] を digit_a[i] + digit_b[i] にする (範囲外の場合は 0)
// 	}
// 	return carry_and_fix(digit_ans); // 2-4 節「繰り上がり計算」の関数です
// }

//入力は文字列として受け取って配列に変換する関数
function stringToBigint(S){
    let N = S.length; // N = (文字列の長さ)
    let digit = [];

    for(let i=0; i<N; i++){
        const char = S[N-i-1];
        const num = parseInt(char);
        digit.push(num);
    }
    return digit;
}
console.log(stringToBigint("12345"));
//足し算　1234 + 5678
//{4,3,2,1} + {8,7,6,5} 
function carryAndFix(digit){
    let N = digit.length;
    for(let i=0; i<N; i++){
        // 繰り上がり処理 (K は繰り上がりの回数)
        if(digit[i] >=10){//どこかが10以上で繰り上がる必要があるとき
            let K = Math.floor(digit[i]/10); //何回繰り上がればいいのか
            digit[i] -=K * 10;
            digit[i+1] += K; //次の位に足す
        }
        //繰り下がり処理 (X-1)%10 + 1
        if(digit[i] < 0){
            let K = Math.floor((-digit[i]-1) / 10 + 1);
            digit[i] += K * 10;
            digit[i + 1] -= K;
        }
    }
    while(digit[N-1] >=10){
        const K = Math.floor(digit[N - 1] / 10);
        digit[N - 1] -= K * 10;
        digit.push(K);
    }
    while (digit.length >= 2 && digit[digit.length - 1] === 0) {
        digit.pop();
    }

}

