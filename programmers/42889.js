function solution(N, stages) {
  var answer = [];
  let clear = new Array(N+2).fill(0);
  let player = new Array(N+2).fill(0);
  let rate = []
  
  for (var i =0; i < stages.length ; i++) {
      if (stages[i] > N) {player[N+1]++}
      else {clear[stages[i]]++};
  }
  
  for (var j = N; j > 0 ; j--) {
      player[j] = clear[j] + player[j+1]
      rate.push([j, clear[j]/player[j]])
  }
  
  answer = rate.sort(function ([a,b], [c,d]) {return d-b||a-c})
              .map(item => item[0])
       
  return answer;
}
