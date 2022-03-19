## Find the unique number
There is an array with some numbers. All numbers are equal except for one. Try to find it!

```js
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
```
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
## Solution:
```js
function findUniq(arr) {
  var uni = Array.from(new Set(arr))
  var c1 = 0
  var c2 = 0
  for(i=0;i<arr.length;i++){
    if(arr[i] == uni[0]){c1++}
    if(arr[i] == uni[1]){c2++}
  }
  if(c1==1){return uni[0]}
  return uni[1]
  }
```