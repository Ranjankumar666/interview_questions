const rob = function (nums, i = 0) {
	if (i == nums.length - 1) return nums[i];

	if (i >= nums.length) return 0;

	total = 0;
	for (let k = i + 2; k < nums.length; k++) {
		total += rob(nums, k);
	}

	return total;
};

console.log(rob([1, 2, 3, 1]));
