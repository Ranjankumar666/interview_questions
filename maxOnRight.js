const solution = (prices) => {
	let stack = [];
	stack.push(-1);
	let n = prices.length;
	let res = Array(n).fill(-1);

	for (let i = n - 1; i >= 0; i--) {
		while (
			stack[stack.length - 1] != -1 &&
			stack[stack.length - 1] < prices[i]
		) {
			stack.pop();
		}

		res[i] = stack[stack.length - 1];
		stack.push(Math.max(stack[stack.length - 1], prices[i]));
	}

	return res;
};

console.log(solution([7, 1, 5, 3, 6, 4]));
