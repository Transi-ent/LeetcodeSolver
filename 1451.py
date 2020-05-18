class Solution:
    def arrangeWords(self, text: str) -> str:
        lyst = text.split(' ')
        lyst[0] = lyst[0].lower()
        lyst.sort(key=len)
        lyst[0] = lyst[0].title()
        return ' '.join(lyst)
