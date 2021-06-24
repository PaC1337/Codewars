var uniqueInOrder=function(iterable){
  arr = []
  if(iterable != []){
    arr.push(iterable[0])
    
    for(i = 1; iterable.length > i; i++){
      if(iterable[i] != arr[arr.length - 1]){
        arr.push(iterable[i])
      }
    }
  }
  return arr
}