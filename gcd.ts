function gcd(a: number, b: number) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function gcdOfOddEvenSums(n: number): number {
  let even = 0;
  let odd = 0;
  for (let i = 1; i <= n * 2; i++) {
    if (i % 2 == 0) {
      even += i;
    } else {
      odd += i;
    }
  }
  // console.log(even);
  // console.log(odd);
  return gcd(even, odd);

};