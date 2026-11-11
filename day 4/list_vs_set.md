**Performance comparison**

- List lookup: 0.00046470 seconds
- Set lookup: 0.00000140 seconds

**Explanation:** List membership testing has a worst-case time complexity of O(n) because Python may need to examine every element until it finds the target. Set membership testing has an average time complexity of O(1) because sets use hashing to locate elements efficiently. Since 99999 is the last element of the list, the list lookup must examine all 100,000 elements, while the set lookup is typically much faster.