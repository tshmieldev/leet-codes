class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator == 0:
            return '0'
        
        sgn =  ''
        if (numerator < 0) ^ (denominator < 0):
            sgn = '-'
        numerator, denominator = abs(numerator), abs(denominator)
        
        whole = sgn + str(numerator // denominator)
        numerator %= denominator
        
        if numerator:
            whole += '.'
        else:
            return whole
        
        seen = {}
        decimal = ""
        
        while numerator:
            if numerator in seen:
                idx = seen[numerator]
                return whole + decimal[:idx] + '(' + decimal[idx:] + ')'

            seen[numerator] = len(decimal)

            numerator *= 10
            digit = numerator // denominator
            decimal += str(digit)
            numerator %= denominator
        
        return whole + decimal