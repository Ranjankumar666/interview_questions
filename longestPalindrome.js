/**
 * @param {string} s
 * @return {string}
 */
const isPalindrome = (S, i , j) => {
	while (i < j) {
		if (S[i] !== S[j]) return false;
		i++;
		j--;
	}
	return true;
};
var longestPalindrome = function (S,i , j,  dp = {}) {
    n = S.length;
    k = `${i},${j}`

	if (dp[k]) return dp[k];

	if ((j - i) === 1 ) {
        return S[i]
    }
    
    if (isPalindrome(S, i, j-1)) {
        dp[k] = S.slice(i, j)
        return dp[k]
    }

    let d = longestPalindrome(S, i+1, j,  dp);
	let b = longestPalindrome(S, i , j-1, dp);
	

	let longest = '';
	if (b.length > longest) longest = b;
	if (d.length > longest) longest = d;

	dp[k] = longest;

	return longest;
};


console.log(longestPalindrome('cbbd', 0, 4))