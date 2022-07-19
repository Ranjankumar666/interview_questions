var calculateMinimumHP = function (mat) {
	let M = mat.length;
	let N = mat[0].length;

	let table = Array(M + 1)
		.fill()
		.map((e) => Array(N + 1).fill(Infinity));

	for (let r = M - 1; r >= 0; r--) {
		for (let c = N - 1; c >= 0; c--) {
			if (r == M - 1 && c == N - 1) {
				table[r][c] = mat[r][c] <= 0 ? -mat[r][c] + 1 : 1;
				continue;
			}
			console.log(mat[r][c]);
			let health = Math.min(table[r + 1][c], table[r][c + 1]) - mat[r][c];

			table[r][c] = health <= 0 ? 1 : health;
		}
	}

	return table[0][0];
};

console.log(calculateMinimumHP([[0, 0]]));
