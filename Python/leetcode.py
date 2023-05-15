
# class Solution(object):
#     def diagonalSum(self,mat):
#         n=len(mat)
#         sum=0
#         for i in range(n):
#             for j in range(n):
#                 if i==j or i+j==n-1:
#                     sum+=mat[i][j]
#         return sum           

# class Solution(object):
#     def isValid(self,s):
#         aizver=[")","]","}"]
#         atver=["(","[","{"] 

#         stack=[]
#         if len(s)%2!=0:
#             return False
#         for char in s:
#             if char in atver and len(stack)==0:
#                 stack.append(char)
#             elif char in atver:
#                 stack.append(char)
#             elif char in aizver and len(stack)==0:
#                 return False
#             elif char in aizver and atver.index(stack[-1])==aizver.index(char):
#                 stack.pop()
#         return len(stack)==0
 
# def isValid(s):
#     if len(s)%2!=0:
#         return False
#     brackets={
#         "(":")",
#         "[":"]",
#         "{":"}"
#     }
#     stack=[]
#     for char in s:
#         if len(stack)==0:
#             if char in brackets:
#                 stack.append(char)
#             else:
#                 return False
#         else:
#             if char in brackets:
#                 stack.append(char)
#             elif char==brackets[stack[-1]]:
#                 stack.pop()
#             else:
#                 return False
    
#     return len(stack)==0

# print(isValid('[]'))

