function* fibonacci(limit) {
    let a = 0, b = 1;
    let count = 0;

    while (count < limit) {
        yield a;
        [a, b] = [b, a + b];
        count++;
    }
}

let fib = fibonacci(10);

for (let num of fib) {
    console.log(num);
}