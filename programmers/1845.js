function solution(nums) {
  var answer = 0;
  const arr = [];
  let flag = false;
  for (var i = 0; i < nums.length; i++) {
    flag = false;
    for (var j = 0; j < arr.length; j++) {
      if (nums[i] === arr[j]) {
        flag = true;
      }
    }
    if (!flag) {
      arr.push(nums[i]);
    }
  }
  if (arr.length > nums.length / 2) {
    answer = nums.length / 2;
  } else {
    answer = arr.length;
  }

  return answer;
}

solution([3, 1, 2, 3]);
solution([3, 3, 3, 2, 2, 4]);
solution([3, 3, 3, 2, 2, 2]);
