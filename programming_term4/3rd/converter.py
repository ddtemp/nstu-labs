class Convert:
    ROMAN_NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    @staticmethod
    def is_roman(roman_numeral):
        import re
        return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_numeral))

    @staticmethod
    def from_roman_to_arabic(roman_numeral):
        normalized_numeral = roman_numeral.upper()
        
        if not Convert.is_roman(roman_numeral):
            return None

        result = 0
        for i in range(len(normalized_numeral)):
            current_value = Convert.ROMAN_NUMERALS[normalized_numeral[i]]
            if i + 1 < len(normalized_numeral) and Convert.ROMAN_NUMERALS[normalized_numeral[i + 1]] > current_value:
                result -= 2 * current_value
            result += current_value

        return result
