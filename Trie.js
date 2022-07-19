class TrieNode {
	constructor() {
		this.children = {};
		this.isWord = false;
	}

	addWord(word) {
		let curr = this;

		for (let ch of word) {
			if (!curr.children[ch]) {
				curr.children[ch] = new TrieNode();
			}

			curr = curr.children[ch];
		}

		curr.isWord = true;
	}

	search(word) {
		let curr = this

		for (let ch of word) {
			if (!curr.children[ch]) return false

			curr = curr.children[ch]
		}

		return curr.isWord

	}
}

function main() {
	let root = new TrieNode();
	let words = ['apple'];

	for (let w of words) {
		root.addWord(w);
	}


	console.log(root.search('apple'))
	console.log(root.search('app'))
}

main();
