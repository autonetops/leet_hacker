#https://leetcode.com/problems/ransom-note/description/

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine) 

        for letter, letterCount in ransomNoteCounter.items():
            #Magazine nao tem uma letra necessaria
            if not magazineCounter.get(letter, False):
                return False
            
            #Magazine nao tem a quantidade de letras suficiente
            if letterCount > magazineCounter.get(letter):
                return False
        
        return True