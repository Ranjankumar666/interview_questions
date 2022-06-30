function coinChnageTable(S, m, n) {
	const table = Array.from({ length: n + 1 })
		.fill()
		.map(() =>
			Array.from({
				length: m,
			})
		);

	for (let val = 0; val <= n; val++) {
		for (let coin = m - 1; coin >= 0; coin--) {
			if (val == 0) {
				table[val][coin] = 1;
			} else {
				const newVal = val - S[coin];
				const t1 = newVal < 0 ? 0 : table[newVal][coin];
				const t2 = coin + 1 >= m ? 0 : table[val][coin + 1];

				table[val][coin] = t1 + t2;
			}
		}
	}

	return table[n][0];
}

function coinChangeTable2(S, m, n) {
	const table = Array.from({ length: n + 1 }).fill(0);

	table[0] = 1;

	for (let target = 1; target <= n; target++) {
		let s = 0;
		for (let num of S) {
			let idx = target - num;

			let res = idx >= 0 ? table[idx] : 0;
			s += res;
		}

		table[target] = s;
	}

	console.log(table);
	return table[n];
}

console.log(coinChangeTable2([1, 2, 3], 3, 4));
