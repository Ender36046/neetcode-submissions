class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {}
        hashmap["}"] = "{"
        hashmap[")"] = "("
        hashmap["]"] = "["
        for i in s:
            if i in ")}]":
                if(len(stack)<=0):
                    return False
                check = stack.pop()
                while(check != hashmap[i]):
                    if(check in "({[" or len(stack) <=0):
                        return False
                    check = stack.pop()
            else:
                stack.append(i)
        if(len(stack) == 0):
            return True
        return False