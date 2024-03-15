class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def calc_space_dist(num_spaces, space_size):
            if num_spaces == 0:
                num_spaces = 1
            spaces = [0]*num_spaces
            for i in range(space_size):
                spaces[i%num_spaces]+=1
            return spaces
        
        def gen_space(space_size):
            return "".join([" " for _ in range(space_size)])
        
        ans = []
        
        curr_words = []
        cur_len = 0
        for word in words:
            if len(word) + cur_len <= maxWidth - len(curr_words):
                curr_words.append(word)
                cur_len += len(word)
            else:
                spaces = calc_space_dist(len(curr_words)-1, maxWidth-cur_len)
                strval = ""
                for i in range(len(curr_words)):
                    strval += curr_words[i]
                    if i < len(spaces):
                        strval += gen_space(spaces[i])
                
                # if len(strval) < maxWidth:
                #     strval += gen_space(maxWidth - len(strval))
                
                curr_words = [word]
                cur_len = len(word)
                ans.append(strval)
        
        if curr_words:
            strval = ""
            strval += " ".join(curr_words)    
            if len(strval) < maxWidth:
                strval += gen_space(maxWidth - len(strval))
                
            ans.append(strval)
        return ans

