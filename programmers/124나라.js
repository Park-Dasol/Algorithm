function solution(n) {
  // var answer = '';
  const answer = [];
  let temp = n
  let olim = 0
  while (temp) {
      if (temp %3 !== 0) {
          answer.push(String(temp%3));
          olim = 0
          temp = Math.floor(temp/3)
      }else {
          answer.push("4")
          olim = 1
          temp = Math.floor(temp/3) -1
      }
      
  }
 
  return  answer.reverse().join('')
}