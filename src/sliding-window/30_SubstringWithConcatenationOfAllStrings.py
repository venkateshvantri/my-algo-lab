class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        print(len(s))
        words_map = {}
        for word in words:
            if word in words_map:
                words_map[word] += 1
            else:
                words_map[word] = 1
        print(words_map)
        words_length = len(words)

        string_map = {}
        word_length = len(words[0])
        for index in range (0, ((words_length) * word_length ), word_length):
            if s[index : index + word_length] in string_map:
                string_map[s[ index : index + word_length]] += 1
            else:
                string_map[s[index :index + word_length]] = 1
        
        print(string_map)

        result = []
        for index in range(0, len(s)-((words_length-1) * word_length), word_length):

            
            if string_map == words_map:
                result.append(index)
            
            if(string_map[s[index:index + word_length]] > 1):
                string_map[s[index:index + word_length]] -= 1
            else:
                string_map.pop(s[index:index + word_length])

            if(s[index + words_length * word_length: index + words_length * word_length + word_length] in string_map):
                string_map[s[index + words_length * word_length: index + words_length * word_length + word_length]] += 1
            else:
                string_map[s[index + words_length * word_length: index + words_length * word_length + word_length]] = 1

            print(string_map)

        return result
    
    
result = Solution().findSubstring("lingmindrabofooowingdingbarrwingmonkoeypoundcake", ["fooo","barr","wing","ding","wing"])
print(result)