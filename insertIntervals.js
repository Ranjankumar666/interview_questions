const merge = (intervals) => {
	const res = [intervals[0]];

	for (const [start, end] of intervals.slice(1)) {
		const [prevStart, prevEnd] = res[res.length - 1];

		if (prevEnd <= start) {
			res[res.length - 1] = [
				Math.min(start, prevStart),
				Math.max(prevEnd, end),
			];
		} else {
			res.push([start, end]);
		}
	}
};

const insert = (intervals, newInterval) => {
	let i = intervals.findIndex((e) => e[0] > newInterval[0]);

	if (i === -1) {
		intervals.push([start, end]);
		return merge(intervals);
	}

	return merge([
		...intervals.slice(0, i),
		[start, end],
		...intervals.slice(i),
	]);
};
