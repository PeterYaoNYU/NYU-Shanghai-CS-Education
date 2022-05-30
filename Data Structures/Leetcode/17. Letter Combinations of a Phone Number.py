from copy import deepcopy
class Solution:
    def letterCombinations(self, digits):
        corres=self.get_dict()
        target=len(digits)
        if target==0:
            return []
        return self.helper(digits, corres,target, res=[], path=[])
        
    def get_dict(self):
        corres={}
        for i in range(8):
            temp=[chr(97+3*i+0), chr(97+3*i+1), chr(97+3*i+2)]
            corres[str(i+2)]=temp
        corres['7']=corres['7']+['s']
        corres['8']=['t','u','v']
        corres['9']=['w','x','y','z']
        return corres

    def helper(self, digits, corres, target, res=[], path=[]):
        if len(path)==target:
            # print(path)
            temp = ''.join(path)
            res.append(temp)
            return res
        if len(digits)==0:
            return
        now=digits[0]
        for i in corres[now]:
            temp=deepcopy(path)
            temp.append(i)
            self.helper(digits[1:], corres, target, res, temp)
        return res

a=Solution()
print(a.letterCombinations('822'))