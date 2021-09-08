function solution(lottos, win_nums) {
    var answer = [];
    
    const sortedMyNums = lottos.sort(function(a,b) { return a-b})
    const sortedWinNums = win_nums.sort(function(a,b) { return a-b})
    
    let wins = 0;
    let myP = 0;
    let winP = 0;
    let zeroC = 0;
    while (myP < sortedMyNums.length && winP < sortedWinNums.length) {
        if (sortedMyNums[myP] === 0 ) {zeroC++; myP++; continue}
        if (sortedWinNums[winP] === sortedMyNums[myP]) {
            wins ++;
            winP++;
            myP++;
        } else if (sortedWinNums[winP] > sortedMyNums[myP]) {
            myP++;
        } else {
            winP++;
        }
    }

    let maxWin = 7 - (zeroC + wins);
     let minWin = 7 - wins;
    if (maxWin === 7) {
        maxWin = 6
    }
    if (minWin === 7) {
        minWin = 6
    }
   
    answer.push(maxWin)
    answer.push(minWin)

    return answer;
}