class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        temp_str = sorted(dic.items(),
                          key=lambda x: (x[1], x[0]),
                          reverse=True)

        re = ""
        for f, el in temp_str:
            re += f * el

        return re