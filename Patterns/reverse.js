let arr = [1,2,3,5,98]
let rev=[]
for(let i=arr.length-1; i>=0;i--){
    rev.push(arr[i])
}
console.log(rev);

rev.forEach((val)=> console.log(val-1));


let f= rev.find(val=> val==1)
// rev=rev.map(val=> val/2)
// rev=rev.map(val=> val*2)

console.log(f);

