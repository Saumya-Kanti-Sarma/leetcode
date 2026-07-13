`
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit. Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
    Input: low = 100, high = 300
    Output: [123,234]

Example 2:
    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]
`

function FirstApproach(low: number, high: number): any {
  const len_low = String(low);
  let initialNumberArray: string[] = [];
  let additionNumberArray: string[] = [];

  for (let i = 1; i <= len_low.length; i++) {
    initialNumberArray.push(String(i));
    additionNumberArray.push("1");
  };
  let initialNumber = Number(initialNumberArray.join(""));
  let additionNumber = Number(additionNumberArray.join(""));

  // console.log(initialNumber);
  // console.log(additionNumber);

  while (initialNumber < low) {
    initialNumber += additionNumber;
    // console.log(initialNumber);
  }

  const result: number[] = [initialNumber];

  while (result[result.length - 1] < high) {
    let num = result[result.length - 1] + additionNumber;

    if ((result[result.length - 1] + 1) % 10 === 0) {
      num = result[0] + Number(`${additionNumber}1`);
      result.push(num);
      continue
    }
    else if (num > high) {
      break
    }
    else {
      result.push(num)
    }
  }
  return result;
};

function SecondApproach(low: number, high: number): number[] {
  const NUMS = '123456789';
  const result = [];
  const lowLength = String(low).length;
  const highLength = String(high).length;

  for (let length = lowLength; length <= highLength; length++) {
    // console.log(length)
    for (let start = 0; start <= NUMS.length - length; start++) {
      const numStr = NUMS.substring(start, start + length);
      const num = Number(numStr);
      // console.log(num);
      if (num >= low && num <= high) {
        result.push(num);
      }
    }
  }

  return result;
}