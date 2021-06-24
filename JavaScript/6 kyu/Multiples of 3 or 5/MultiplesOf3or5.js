function solution(number){
  sol = 0
  for(i = 0; number > i; i++){
    if((i % 3) == 0 || (i % 5) == 0){
      sol += i
    }
  }
  return sol
}