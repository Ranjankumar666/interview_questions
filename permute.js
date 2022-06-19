const permute = (arr) => {
	let results = [];

	let go = (current) => {
		if (current.length === arr.length) {
			results.push(current);
			return;
		}

		for (let num of arr) {
			if (!current.includes(num)) {
				go([...current, num]);
			}
		}
	};

	go([]);

	return results;
};

console.log(permute([1, 2]));
