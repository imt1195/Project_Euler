//sieve of Eratosthenes, finds and returns all prime numbers between 2 and an inputed number
function Eratosthenes(num){
    let arr = Array(num).fill(true);
    let retArr = [];
    let sqrtNum = Math.sqrt(num);
    for(let i=2; i<=sqrtNum; i++){
        if(arr[i] === true){
            for(let j=2; i * j<num; j++){
                arr[i*j] = false;
            }
        }
    }
    for(let i=2; i<num; i++){
        if(arr[i] === true){
            retArr.push(i);
        }
    }
    return retArr;
}