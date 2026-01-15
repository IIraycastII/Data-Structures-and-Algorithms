class Solution(object):
    def reverse(self, x):
        list_1 = []
        a = ""

        if "-" in str(x):
            for i in str(x):
                list_1.append(i)

            list_1.remove("-")

            for i in list_1:
                a += str(i)
            a = "-" + str(a)[::-1]
            rev = int(a)
            if rev > -2 ** 31 and rev < 2 ** 31 - 1:
                return rev
            else:
                return 0
        elif "-" not in str(x):
            rev = int(str(x)[::-1])
            if rev > -2 ** 31 and rev < 2 ** 31 - 1:
                return rev
            else:
                return 0
