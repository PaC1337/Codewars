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