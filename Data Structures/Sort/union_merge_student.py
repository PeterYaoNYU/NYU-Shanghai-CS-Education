def union_merge(S1, S2):
  """
  Input: S1 and S2 are sorted lissy, but can contain duplicated values
  Output: Return a lissy that are sorted but with duplicates removed.
  """
  pt1=0
  pt2=0
  ans=[]
  while pt1<len(S1) and pt2<len(S2):
    if S1[pt1]<=S2[pt2]:
      if not ans:
        ans.append(S1[pt1])
      elif ans and ans[-1]!=S1[pt1]:
        ans.append(S1[pt1])
      pt1+=1
    else:
      if not ans:
        ans.append(S2[pt2])
      elif ans and ans[-1]!=S2[pt2]:
        ans.append(S2[pt2])
      pt2+=1
    # print(ans)
      
  if pt1<len(S1):
    for i in range(pt1, len(S1)):
      if ans and S1[i]!=ans[-1]:
        ans.append(S1[pt1])
  elif pt2<len(S2):
    for i in range (pt2, len(S2)):
      if ans and S2[i]!=ans[-1]:
        ans.append(S2[i])
  return ans

        
        
    
    

if __name__ == '__main__':
  S1 = [1,1,1,1,2,2,2,3,4,6,8,8,8]
  S2 = [2,2,2,3,4,6,8,8,8]
  S = union_merge(S1, S2) # Expect: [1,2,3,4,6,8]
  # print(S)
