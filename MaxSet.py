import sys
 
def max_independent_set(nums, i, n, previous=-sys.maxsize):
  #If all the elements are processed this is the base case
  if i == n:
    return []
 
  #recur the current element
  ignore = max_independent_set(nums, i+1, n, previous)
 
  keep = []
 
  #put current element in keep if its not adjacent to the previous element
  if previous + 1 != i:
    keep = max_independent_set(nums, i+1, n, i)
    keep.append(nums[i])
    
  #return maximum sum we get by keeping or ignoreing current item
  if sum(keep) > sum(ignore):
    #print(sum(keep))
    return keep
  else:
  	return ignore
 
 
if __name__ == '__main__':
 
    nums = [-1, -1, -10, -34] 
    out=max_independent_set(nums, 0, len(nums))
    print('The maximum sum is', out,sum(out))
