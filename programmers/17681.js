function solution(n, arr1, arr2) {
  var answer = [];
  arr1 = binary(n, arr1)
  arr2 = binary(n, arr2)
  for (var i = 0; i < n ; i++) {
    let temp = []
    for (var j =0; j <n ; j++) { 
      if (arr1[i][j] == 1 || arr2[i][j] == 1) {
        temp.push('#')
      } else {
        temp.push(' ')
      }
    }
    const word = temp.join('')
    answer.push(word)
  }
  console.log(answer)
  return answer;
}


function binary(n, arr) {
  for (var i=0; i < n; i++) {
    const temp = []
    let num = arr[i]
    for (var j = 0; j < n-1; j++) {
      const remainder = num % 2
      num = parseInt(num / 2)
      temp.splice(0, 0, remainder)
    }
    temp.splice(0, 0,num)
    arr[i] = temp
  }
  return arr
}



solution(5, 	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28] )