// board
// [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
// moves
// [1,5,3,5,1,2,1,4]	
// result 4


function solution(board, moves) {
  var answer = 0;
  var basket = [];
  const l = board.length

  for (var i = 0; i < moves.length; i++) {
    num = moves[i] -1

    for (j = 0; j < l; j ++ ) {

      if (board[j][num] != 0 ) {
        temp = board[j][num];
        move(temp)
        board[j][num] = parseInt(0);
        break;
      }
    }
  }
  function move(item) {
    var last = basket.length -1
    if (last >= 0 && basket[last] === item) {
      basket.pop()
      answer = answer + 2
    } else {
        basket.push(item)   
    }

  }

  console.log(answer)
  return answer;
}

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],  [1,5,3,5,1,2,1,4])


