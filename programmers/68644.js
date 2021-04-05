function solution(numbers) {
  var answer = [];
  let everyanswer = [];
  for (var i=0; i < numbers.length-1; i++) {
    for (var j=i+1; j < numbers.length; j++) {
      let temp = numbers[i] + numbers[j];
      everyanswer.push(temp)
    }
  }

  const clean = new Set(everyanswer);
  answer = [...clean]


  answer.sort(function(a,b) {
    return a-b;
  })

  console.log(answer)
  

  return answer;
}


solution([2,1,3,4,1])