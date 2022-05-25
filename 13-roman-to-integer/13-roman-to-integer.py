class Solution:
    dict_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int:
        ele_stack = []
        for i,val in enumerate(s.upper()):
            if i:
                if ele_stack[-1] < self.dict_roman[val]:
                    ele_stack[-1] = int('-'+str(ele_stack[-1]))
                ele_stack.append(self.dict_roman[val])
            else:
                ele_stack.append(self.dict_roman[val])
                
        return sum(ele_stack)