
function solution(string) {
  newstring = ''
  for(l of string){
    if(l == l.toUpperCase()){
      newstring += ' '
      newstring += l
    }
    else{
      newstring += l
    }
  }
  return newstring
    
}
