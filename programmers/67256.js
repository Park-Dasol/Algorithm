function solution(numbers, hand) {
  var answer = '';  
  const phone = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
  let result = []
  let leftP = [0, 3];
  let rightP = [2, 3];
  let idx = '';
  let leftD = 0;
  let rightD = 0;
  for (var t = 0; t < numbers.length; t++) {
    const n = numbers[t]

    if(phone[0].includes(n)) {

      result.push('L')
      leftP[0] = 0
      leftP[1] = phone[0].indexOf(n)
    } else if (phone[2].includes(n)) {
      result.push('R')

      rightP[0] = 2
      rightP[1] = phone[2].indexOf(n)
    } else {
      idx = phone[1].indexOf(n)

      leftD = Math.abs(1-leftP[0]) + Math.abs(idx - leftP[1])
      rightD = Math.abs(1-rightP[0]) + Math.abs(idx - rightP[1])

      if (rightD > leftD) {

        result.push('L')
        leftP[0] = 1
        leftP[1] = idx
      } else if (leftD > rightD) {

        result.push('R')
        rightP[0] = 1
        rightP[1] = idx
      } else {
        if (hand==="right") {

          result.push('R')
          rightP[0] = 1
          rightP[1] = idx
        } else {
          result.push('L')

          leftP[0] = 1
          leftP[1] = idx
        }
      }
    }

  }

  answer = result.join('')
  return answer;
}


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")