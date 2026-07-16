# ========================= original solution(wrong) ===========================
class Solution(object):
    def groupAnagrams(self, strs):
        all_word = {}
        for word in strs:
            single = []
            for i in word:
                single.append(i)
            if word not in all_word:
                all_word[word] = [single,1] # The biggest mistake: using the original word as the dictionary key
            else:
                all_word[word][1] += 1
        print(all_word)
        answers = []
        for i,v in all_word.items():
            lis = []
            lis.append(i)
            for a,b in all_word.items(): # nested loops
                if sorted(v[0]) == sorted(b[0]) and i != a:
                    #for t in range(b[1]+1):
                        #lis.append(a)
                    lis.append(a)
            if not answers:
                answers.append(sorted(lis))
            else:
                if sorted(lis) not in answers:
                    answers.append(sorted(lis))
        return answers
"""for every word:
    calculate key
    put into dictionary"""
# ============================= revise ===================================

class Solution(object):
    def groupAnagrams(self, strs):

        all_word = {}

        for word in strs:
            single = []

            for i in word:
                single.append(i)

            key = "".join(sorted(single))

            if key not in all_word:
                all_word[key] = [word]
            else:
                all_word[key].append(word)

        answers = []

        for i,v in all_word.items():
            answers.append(v)

        return answers

# =========================== the optimal solution ==============================
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())