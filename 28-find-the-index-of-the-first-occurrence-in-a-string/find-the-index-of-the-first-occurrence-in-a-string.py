class Solution(object):
    def strStr(self, haystack, needle):
        text_haystack = 0
        text_needle = 0
        original = 0

        if len(haystack) > 1 and len(haystack) >= len(needle):
            while text_haystack != len(haystack):
                if needle[text_needle] == haystack[text_haystack]:
                    text_haystack += 1
                    text_needle += 1

                    if text_needle == len(needle):
                        return original
                        break
                elif haystack[text_haystack] != needle[text_needle]:
                    original += 1
                    text_haystack = original
                    text_needle = 0
            return -1
        elif len(haystack) == 1 and len(needle) == 1:
            if haystack[0] == needle[0]:
                return 0
            return -1
        elif len(needle) == 1:
            while text_haystack !=  len(haystack):
                if needle[text_needle] == haystack[text_haystack]:
                    return text_haystack
                elif haystack[text_haystack] != needle[text_needle]:
                    text_haystack += 1
            return -1
        return -1