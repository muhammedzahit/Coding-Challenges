Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

    Example 1:

    Input: nums = [1,2,3]
    Output: 6

    Example 2:

    Input: nums = [1,2,3,4]
    Output: 24

    Example 3:

    Input: nums = [-1,-2,-3]
    Output: -6

 

Constraints:

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

# Solution

13 ms

```java
class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int len = nums.length;
        return Math.max(Math.max(
            nums[len-1] * nums[len-2] * nums[len-3],
            nums[0] * nums[1] * nums[2]),
            nums[0] * nums[1] * nums[len-1]
        );
    }
}
```

![img](a.png)

Or implement ABS to all values and pick three largest values.
