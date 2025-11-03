Problem 2:
When approaching this problem, my thought process was straightforward:
to find the smallest number of elements whose sum exceeds T, the most efficient way is to use the largest numbers first.
I started by sorting the array in descending order. This way, the biggest numbers come first, allowing us to reach the target sum faster with fewer elements.
Then I simply added elements one by one from the largest to the smallest, keeping count until the running total exceeded T.
The algorithm was simple and effective: sort, then accumulate until the sum passes T.
I didn't encounter significant challenges with this problem since the greedy approach naturally fits this scenario.
The solution handled all test cases correctly, including the provided examples.

Problem 3:
When building this algorithm, my initial idea was to use the property of perpendicular vectors: 
treat each point as a right angle vertex, calculate vectors to other points, normalize them, 
and count how many vectors point in each direction. 
For each vector, find its perpendicular vector and count the combinations, then divide the total by 2 to remove duplicates.
This approach seemed mathematically sound, but in practice, it gave incorrect results. 
I then tried to fix it by tracking processed vector pairs to avoid double-counting, instead of simply dividing by 2.
However, a small error remained.
I acknowledge the error in my algorithm. For the third test file, the correct answer should be 5294, but my code outputs 5295.
Despite trying various improvements to the vector handling and matching logic, I couldn't eliminate this difference of 1.
I'm still unsure why this happens—there might be edge cases or counting issues I haven't identified.