function maxProduct(arr) {
	let max_e = arr[0];
	let min_e = arr[0];
	let global_max = arr[0];

	for (let i = 1; i < arr.length; i++) {
		let num = arr[i];
		const temp = max_e;

		max_e = Math.max(num, num * max_e, num * min_e);
		min_e = Math.min(num, num * temp, num * min_e);

		global_max = Math.max(global_max, max_e);
	}

	return BigInt(global_max);
}

console.log(
	maxProduct(
		'3 12 15 23 33 -35 30 -40 -30 -30 -30 26 28'.split(' ').map((x) => +x)
	)
);
