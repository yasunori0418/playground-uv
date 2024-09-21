class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1:
            return s



assert Solution().convert("A", 1) == "A"

# PAYPALISHIRING
#
#
# P     A     H     N
#
# A  P  L  S  I  I  G
#
# Y     I     R  
#
#
# PAHNAPLSIIGYIR
# assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"


# PAYPALISHIRING
#
#
# P        I        N
#
# A     L  S     I  G
#
# Y  A     H  R
#
# P        I  
#
#
# PINALSIGYAHRPI
# assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


# PAYPALISHIRING
#
#
# P           H  
#
# A        S  I  
#
# Y     I     R  
#
# P  L        I  G
#
# A           N  
#
#
# PHASIYIRPLIGAN
# assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
