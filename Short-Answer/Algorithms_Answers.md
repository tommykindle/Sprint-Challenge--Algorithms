#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
 The time complexity of A would be O(n)
 Justification : there is a while loop of n * n * n but gets updated with n * n  so it would be linear time based on n

b)
The time complexity of B would be O(n log n)
due to the while loop's range it would be n log n however it might be base to because of the J*=2

c)
The time complexity of C would be O(n) even though there is recusion there is still only n operations


## Exercise II
I think I would want to implement a Binary Search to find F
start by looking for the middle value for n If the eggs break then take the middle value of 0 to high-low / 2-1. If the eggs didn't break I would do the same processs with the upper segment but it would be hight-low /2 +1 to n. Then I could repeat the process until F was found and the run time of binary search would be O(log n)