import collections
import re
from typing import List

import self as self

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

class Solution:
    def mostCommomWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
        count = collections.defaultdict(int)
        for word in words:
            count[word] += 1
        return count.most_common(1)[0][0]

taro=Solution()
taro.mostCommomWord(paragraph,banned)
