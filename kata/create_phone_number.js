function createPhoneNumber(numbers) {
  var phone = "(";
  
  for (var i = 0; i < 3; i++) {
    phone += numbers[i].toString();
  }
  
  phone += ") ";
  
  for (var j = 3; j < 6; j++) {
    phone += numbers[j].toString();
  }
  
  phone += "-";
  
  for (var k = 6; k < 10; k++) {
    phone += numbers[k].toString();
  }
  
  return phone
}