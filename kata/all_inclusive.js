// Description:

// Input:
// a string strng
// an array of strings arr

// Output of function containAllRots:
// a boolean true if all rotations of strng are included in arr
// false otherwise

// Examples:
// contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"])
// -> true

// contain_all_rots("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy",
//                              "pyAjylv", "vpyAjyl", "ipywee"]) -> false

// Note:
// Though not correct in a mathematical sense
// we will consider that there are no rotations of strng == ""
// and for any array arr: contain_all_rots("", arr) --> true

function containAllRots(strng, arr) {
  if (strng == "" && arr.length > 0) {
    return true
  }
  
  for (i = 0; i < strng.length; i++) {
    first_letter = strng.charAt(0)
    strng = strng.substr(1)
    strng += first_letter
      if (arr.indexOf(strng) <= -1) {
        return false
      }
   }
   
   return true
}