function solution(lines) {
  var answer = 0;
  const work = []
  let maxCnt = 0
  for (var i = 0; i < lines.length; i++) {
      const line = lines[i].split(' ');
      const endList = line[1].split(':');
      let end = 0
      for (var t = 2; t >= 0; t--) {
        end += 60 ** t * endList[2-t]
      }
      parseFloat(end).toFixed(3)
      const start = parseFloat((line[2].slice(0, -1))- 0.001).toFixed(3)
      work.push([(end - start), end])
  }
  // console.log(work)
  for (let j = 0 ; j <work.length-1; j++) {
    let cnt = 0

    for (let l = j+1; l < work.length; l++ ){
      if ((work[j][1] + 1 - 0.001).toFixed(3) >= work[l][0]) {
        cnt += 1
      }
    }
    if (cnt > maxCnt) {
      maxCnt = cnt
    }
  }
  console.log(maxCnt +1)
  return maxCnt + 1;
}

// solution([
//   "2016-09-15 01:00:04.002 2.0s",
//   "2016-09-15 01:00:07.000 2s"
//   ])


// solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
// solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])