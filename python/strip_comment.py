import re
def solution(string,markers):
	markers = r'|'.join(re.escape(marker) for marker in markers)
    words = [re.split(markers, word)[0].rstrip() for word in text.split('\n')]
    return '\n'.join(words)
print( solution('pears apples , watermelons\n? , avocados strawberries cherries lemons\navocados watermelons watermelons\nlemons\nbananas pears apples .', ["'", '?', '-', '#', '=', '!', '@', '^', '.']))