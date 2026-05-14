class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        senate = list(senate)

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            rTurn = R.popleft()
            dTurn = D.popleft()

            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))
        
        return "Radiant" if R else "Dire"