const fractionalKnapsack = (Items, W, n) => {
	Items = Items.sort((a, b) => a.weight - b.weight);
	let V = 0;
	let i = 0;

	while (i < n && W > 0) {
		const item = Items[i];

		const { value: val, weight: wt } = item;

		if (wt > W) {
	
            V += (W * val) / wt;
            W -= W;
		} else {
			W -= wt;
			V += val;
		}

		i += 1;
	}

	return V;
};

class Item {
	constructor(value, weight) {
		this.value = value;
		this.weight = weight;
	}
}

const items = [new Item(60, 10), new Item(100, 20), new Item(120, 30)];

console.log(fractionalKnapsack(items, 50, items.length));
