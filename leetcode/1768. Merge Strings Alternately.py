#Solucao 1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_menor = min(len(word1), len(word2))
        
        merged = ''
        for i in range(len_menor):
            merged += word1[i]+word2[i]
        
        merged += word1[len_menor:] + word2[len_menor:]

        return merged