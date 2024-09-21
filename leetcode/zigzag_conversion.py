class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1:
            return s



assert Solution().convert("A", 1) == "A"

# PAYPALISHIRING
#
# 1     5     9     13
# P     A     H     N
#
# 2  4  6  8  10 12 14
# A  P  L  S  I  I  G
#
# 3     7     11
# Y     I     R
#
#
# PAHNAPLSIIGYIR
# assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"


# PAYPALISHIRING
#
# 1        7        13
# P        I        N
#
# 2     6  8     12 14
# A     L  S     I  G
#
# 3  5     9  11
# Y  A     H  R
#
# 4        10
# P        I
#
#
# PINALSIGYAHRPI
# assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


# PAYPALISHIRING
#
# 1           9
# P           H
#
# 2        8  10
# A        S  I
#
# 3     7     11
# Y     I     R
#
# 4  6        12 14
# P  L        I  G
#
# 5           13
# A           N
#
#
# PHASIYIRPLIGAN
# assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
