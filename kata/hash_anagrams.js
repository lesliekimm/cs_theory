// Description:
// Given a hash of letters and the number of times they occur, recreate all
// of the possible anagram combinations that could be created using all of
// the letters, sorted alphabetically.

// The inputs will never include numbers, spaces or any special characters,
// only lowercase letters a-z.

// E.g. get_words({2=>["a"], 1=>["b", "c"]})
// => ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca",
//     "bcaa", "caab", "caba", "cbaa"]



function getWords(hash) {
  all_letters = ""

  for (var key in hash) {
    for (var i in hash[key]) {
      all_letters += Array(parseInt(key)+1).join(hash[key][i])
    }    
  }

  return permutations(all_letters);
}

function permutations(string) {
  if (string.length == 0) {
    return [string]
  }
  else {
    prev_s = permutations(string.slice(1, string.length))
    res_s = []
    for (var i = 0; i < prev_s.length; i++) {
      for (var j = 0; j < string.length; j++) {
        new_s = prev_s[i].slice(0, j) + string.charAt(0) + prev_s[i].slice(j, string.length - 1)
        if (res_s.indexOf(new_s) < 0) {
          res_s.push(new_s)
        }
      }
    }
  }
  res_s.sort()
  return res_s
}

// Kata tests fail bc it times out
function test_getWords() {
  // ["abc", "acb", "bac", "bca", "cab", "cba"]
  console.log(getWords({1:["a", "b", "c"]}));
  // ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])
  console.log(getWords({2:["a"], 1:["b", "c"]}));
}

test_getWords()