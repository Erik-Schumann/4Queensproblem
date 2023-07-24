# 4Queensproblem

In the 4 Queens Problem each quuen has 3 constraints to th eother queens:
1. There should not be another queen in the same column (we prevent this by modelliung that each queen will be able to place into its individual column)
2. There should not be another queen in the same row
3. There should not be another queen in the same diagonal

The idea of the code it to incrementially check the graph. E.g. when the first queen is put into y= 1 the second queen is not allowed to be placed into y = 1 (contraint 2) or y = 2 (constraint 3). When queen #2 already does not fulfill the constraints it is not useful to check the combinations of queen #3 and #4. 
Goind into deeper level requires to check more queens, since there are more on the board.
Algorithm solves:
Solution --> 2   4   1   3
Solution --> 3   1   4   2

The following picture displays the idea of the algorithm

![image](https://github.com/Erik-Schumann/4Queensproblem/assets/49512734/6438a94f-3b95-42f8-b3bf-58a406eaa47b)

