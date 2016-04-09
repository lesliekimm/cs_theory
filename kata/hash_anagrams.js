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
      all_letters += (hash[key][i].repeat(key));
    }    
  }

  return permutations(all_letters);
}

function permutations(string) {
  if (string.length == 1) {
    return [string]
  }
  else {
    // permute
  }
}

function test_getWords() {
  // ["abc", "acb", "bac", "bca", "cab", "cba"]
  console.log(getWords({1:["a", "b", "c"]}));
  // ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])
  console.log(getWords({2:["a"], 1:["b", "c"]}));
}

test_getWords()