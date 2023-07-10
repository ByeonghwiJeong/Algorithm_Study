function solution(s, n) {
  let answer = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      answer += " ";
      continue;
    }
    const charCode = s.charCodeAt(i);
    let newCharCode = null;
    if (charCode >= 65 && charCode <= 90) {
      newCharCode = charCode + n;
      if (newCharCode > 90) newCharCode -= 26;
    } else {
      newCharCode = charCode + n;
      if (newCharCode > 122) newCharCode -= 26;
    }
    answer += String.fromCharCode(newCharCode);
  }
  return answer;
}

/**
 * ! 암기
 * ? {String}.charCodeAt({int})
 * * 문자열.charCodeAt(idx) : 문자열의 idx번째의 아스키코드
 * ? String.fromCharCode({int})
 * * 아스키코드 역변환
 * ? < 아스키 코드 >
 * * 65 : 대문자 A
 * * 90 : 대문자 Z
 * * 97 : 소문자 a
 * * 122 : 소문자 z
 */
