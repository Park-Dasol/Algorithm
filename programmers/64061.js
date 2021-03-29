function solution(board, moves) {
  var answer = 0;
  return answer;
}



// board
// [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
// moves
// [1,5,3,5,1,2,1,4]	
// result 4

// for (var i = 0; i < lines.length; i++) {
//   const line = lines[i].split(' ');
//   const endList = line[1].split(':');
//   let end = 0
//   for (var t = 2; t >= 0; t--) {
//     end += 60 ** t * endList[2-t]
//   }
//   parseFloat(end).toFixed(3)
//   const start = parseFloat((line[2].slice(0, -1))- 0.001).toFixed(3)
//   work.push([(end - start), end])
// }