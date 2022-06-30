function lc(arr, i, dp) {
	if (dp[i]) return dp[i];

	if (i >= arr) return i + 1;

	let max = 0;
	for (let k = i + 1; k < arr.length; k++) {
		if (arr[i] - arr[k] == 1) {
			let count = 1 + lc(arr, i);
			max = Math.max(count, max);
		}
	}

	dp[i] = max;
	return max;
}

function driver(arr) {
	arr = arr.sort((a, b) => a - b);
	const dp = Array.from({
		length: arr.length,
	}).fill(false);

	return lc(arr, 0, dp);
}

console.log(driver([3, -1, 0, 4, 5, 6]));
