## Break camelCase
Complete the solution so that the function will break up camel casing, using a space between words.

**Example**
```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

## Solution:
```js
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
```