class Solution:
    def reverse(self, x: int) -> int:
        neg_flag = False
        max_val = pow(2,31)
        if x < 0:
            neg_flag = True
            
        final_val =0
        x = abs(x)
        while x!= 0:
            digit = abs(x%10)
            final_val = (final_val * 10) + digit
            x = x//10

        if neg_flag:
            final_val = -abs(final_val)

        if final_val >= -abs(max_val) and final_val <= max_val-1:
            return final_val
        else:
            return 0