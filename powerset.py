#citation:
#date: 10/22/21
#code made from pseudocode in canvas
#link: https://canvas.oregonstate.edu/courses/1830227/pages/exploration-backtracking?module_item_id=21389065

def powerset_helper(pointer, choices_made,arr, result):
  if (pointer == 0):
    #result.append(choices_made) #make a deep copy since we are working with objects
    print(choices_made)
    return
  
  choices_made.append(arr[pointer-1]) #append arr[pointer] to choices_made
  powerset_helper(pointer-1, choices_made, arr, result)
  
  #backtracking
  choices_made.pop() #remove last element added to choices_made
  
  powerset_helper(pointer-1, choices_made, arr, result)

def powerset(arr):
  result = []
  powerset_helper(len(arr), [], arr, result)
  #return result
    
if __name__ == '__main__':
  
  arr=[1,2,3]
  powerset(arr)
  
#resolved Yay
#Input: [1,2,3]
#What Output Should be: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
#What I get: 
'''
[3, 2, 1]
[3, 2]
[3, 1]
[3]
[2, 1]
[2]
[1]
[]
[]
'''