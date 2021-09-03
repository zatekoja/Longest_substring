def solution(s: str):
        queue = []
        idx = 0
        result = 0

        while idx < len(s):
            if s[idx] not in queue:
                queue.append(s[idx])
                idx += 1
                result = max(len(queue), result)
            else:
                val = queue.pop(0)
                while val is not s[idx]:
                    val = queue.pop(0)
                queue.append(s[idx])
                idx += 1
        return result
"https://leetcode.com/problems/longest-substring-without-repeating-characters/"