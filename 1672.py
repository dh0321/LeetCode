class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        totalBalanceList = []

        for acc in accounts:
            totalBalance = 0
            for balance in acc:
                totalBalance += balance
                totalBalanceList.append(totalBalance)

        maxAcc = max(totalBalanceList)
        return maxAcc

'''
Solution1.
  def maximumWealth(self, accounts: List[List[int]]) -> int:
      return max(sum(acc) for acc in accounts)

Solution2.
  def maximumWealth(self, accounts: List[List[int]]) -> int:
	  maxWealth = 0
	  for i in range(len(accounts)):
		  totalWealth = sum(accounts[i])
		  maxWealth = max(maxWealth, totalWealth)
	  return maxWealth


Solution3.
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthy_person=0
        for balance in accounts:
            total=sum(balance)
            wealthy_person=max(wealthy_person,total)
        return wealthy_person
'''
