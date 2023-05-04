class Solution:
    def sortSentence(self, s: str) -> str:
        unsortedsentence = s.split(' ')
        sortedsentence = []
        position = []
        string_to_return = ""
        for i in unsortedsentence:
            position.append(int(i[-1:]))
            sortedsentence.append(" ")
        for j in range(1,len(position)+1):
            #print(unsortedsentence,(position[j-1])-1)
            val = unsortedsentence[j-1]
            #print(val)
            sortedsentence[(position[j-1])-1] = val[:-1]
        string_to_return = (" ".join(sortedsentence))
        return(string_to_return)