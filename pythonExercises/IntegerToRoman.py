class Solution:
    dictionary={
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    def intToRoman(self, num: int) -> str:
        result=""
        for value,symbol in self.dictionary.items():
            while num>=value:
                result+=symbol
                num-=value
        return result

    
