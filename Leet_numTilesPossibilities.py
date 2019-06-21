
def numTilePossibilities(tiles):
	memo = set()     # avoid repeated combinations
	def helper(cur, eles):
		if cur in memo:
			return
		if cur not in memo or not eles:
			memo.add(cur)
		for i in range(len(eles)):
			helper(cur + eles[i], eles[:i] + eles[i+1:])
		return
	helper('', tiles)
	return len(memo) - 1    # remove empty string in memo


titles = "AAABBC"
numTilePossibilities(titles)