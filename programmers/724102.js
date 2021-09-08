function solution(new_id) {
  var answer = '';
  let letter ='';
  for(var i = 0; i < new_id.length; i++) {
      letter = new_id[i]
      if (answer[answer.length -1]==='.' && letter==='.') {continue}
      if (letter.toLowerCase() !== letter.toUpperCase()) {
          answer +=letter.toLowerCase();
      } else if (letter === '-' || letter==='_' || letter==='.') {
          answer += letter;
      } else if (Number.isInteger(parseInt(letter))) {
          answer += letter;
      }
  }
  
  while (answer.startsWith('.') ) { 
      if (answer.startsWith('.')) { answer = answer.slice(1)};    
  }
  answer = answer.slice(0, 15)
  while (answer.endsWith('.')) {
      if (answer.endsWith('.')) {
      answer = answer.slice(0,  answer.lastIndexOf('.'))
      } 
  }
  
  if (answer.length ===0) {
      answer = 'aaa'
  } else if (answer.length < 3) {
      const newL = answer[answer.length -1]
      const times = 3 - answer.length;
      answer += newL.repeat(times);
  }
          
  return answer;
}