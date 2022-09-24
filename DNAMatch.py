
#citation
#I got help with this topdown function from the coin demo/makechangeBF.py that was done during demo also got insparation from geeks to geeks github example
#link: https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-makeChangeBruteForce.py
#https://canvas.oregonstate.edu/courses/1830227/pages/exploration-dynamic-programming-change-making-problem?module_item_id=21389053
#https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-lcs_bruteforce.py
#recursive
def dna_match_topdown(DNA1, DNA2,one,two):
  if one == 0 or two == 0:
    #the strings have no length....
    return 0
  elif DNA1[one-1] == DNA2[two-1]:
    one=one-1
    two=two-1
    return 1 + dna_match_topdown(DNA1,DNA2,one,two)
  else:
    return max(dna_match_topdown(DNA1,DNA2,one,two-1), dna_match_topdown(DNA1,DNA2,one-1,two))

#citation
#function based on makechange_bottomup.py on github/canvas
#link: https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-makechange_bottomup.py
#also got help from the hint code
#link: https://canvas.oregonstate.edu/courses/1830227/pages/exploration-dynamic-programming-longest-common-subsequence-problem?module_item_id=21389054
#iterative
def dna_match_bottomup(DNA1, DNA2):
  one = len(DNA1)
  two = len(DNA2)
  
  arr = [[None]*(one+1) for i in range(two+1)]
  
  for i in range(two+1):
    for j in range(one+1):
      if i == 0 or j == 0:
        arr[i][j] = 0
      elif DNA1[i-1] == DNA2[j-1]:
        arr[i][j] = arr[i-1][j-1]+1
      else:
        arr[i][j] = max(arr[i-1][j] , arr[i][j-1])
      
  return arr[one][two]
  
  

if __name__ == '__main__':
  DNA1 = "ATAGTTCCGTCAAA"
  DNA2 = "GTGTTCCCGTCAAA"
  
  one = len(DNA1)
  two = len(DNA2)

  print("Longest character length possible using Top-Down: ", dna_match_topdown(DNA1, DNA2, one, two))
  print("Longest character length possible using Bottom-Up: ", dna_match_bottomup(DNA1, DNA2)) 