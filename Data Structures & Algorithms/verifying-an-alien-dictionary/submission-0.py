class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #first different chr
        #if word A is prefix word B, word B must be after word A

        orderInd = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                   return False

                if w1[j] != w2[j]:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break

        return True