// Even or Odd

function even_or_odd(number) {
    let isEven = number % 2 === 0 ? "Even" : "Odd";
    return isEven;
  }



// Convert Number to Reversed Array of Digits

function digitize(n) {
    let listDigits = n.toString().split("")
    let revList = listDigits.reverse()
    revList = revList.map(function(numString) {
      return parseInt(numString)
    })
    return revList
  }



// Remove First and Last Character

function removeChar(str){
    const new_str = str.slice(1, str.length - 1)
    return new_str
   };



// Returning Strings

function greet(name){
    return `Hello, ${name} how are you doing today?`
  }



// String Repeat

function repeatStr (n, s) {
  
  return s.repeat(n);
}



// Calculate BMI

function bmi(weight, height) {
    let bmi = weight / (height **2);
    if (bmi <= 18.5) {
      return "Underweight"
    } else if (bmi>18.5 && bmi<=25) {
      return "Normal"
    } else if (bmi>25 && bmi<=30) {
      return "Overweight"
    } else if (bmi>30) {
      return "Obese"
    }
  };



  // HTML Dynamic Color String Generation

  const generateColor = function() {
    let hex = '0123456789abcdefABCDEF'

    let randomList = '#'
    for (let i=0 ; i<6 ; i++) {
        random = hex[Math.floor(Math.random() * hex.length)]
        randomList += random;
    }
    return randomList;
}