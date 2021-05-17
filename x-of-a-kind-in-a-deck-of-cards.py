from typing import List
import random


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        tmp = dict.fromkeys(deck, int())
        print(tmp)
        for i in deck:
            for j in tmp:
                if i == j:
                    tmp[j] += 1

        print(tmp)
        # check = tmp[deck[0]]
        # for i in tmp.values():
        #     if i == 1 or i % check != 0:
        #         return False
        # return True


c = Solution()
print(c.hasGroupsSizeX([1, 2, 1 , 1]))
