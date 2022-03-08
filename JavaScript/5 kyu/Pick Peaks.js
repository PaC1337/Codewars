function pickPeaks(arr){
  
  var arrPeaks = {pos: [], peaks: []};
  
  if(arr == []){
    return arrPeaks;
  }
  
  let localPos = 0
  let localVal = 0
    
  for(let i = 1; i < arr.length; i++){
    if(arr[i] > arr[i-1]){
      localPos = i
      localVal = arr[i]
      }
    else if(arr[i] == arr[i-1]){
      
    }
    else if(arr[i] < arr[i-1]){
      if(localPos > 0){
        arrPeaks.pos.push(localPos);
        arrPeaks.peaks.push(localVal);
        localPos = 0
      }
    }  
  }
  return arrPeaks
}