package slice

func MaximumWealth(accounts [][]int) int {
	accountsAsset := make([]int, len(accounts))
	for i, account := range accounts {
		sum := 0
		for _, amount := range account {
			sum += amount
		}
		accountsAsset[i] = sum
	}

	maxAsset := 0
	for _, asset := range accountsAsset {
		if asset > maxAsset {
			maxAsset = asset
		}
	}

	return maxAsset
}
