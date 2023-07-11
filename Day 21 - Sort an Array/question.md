# Question 

[Question Link](https://leetcode.com/problems/sort-an-array/)

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
    Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
    Explanation: Note that the values of nums are not necessairly unique.

Constraints:

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104

# Solution-1

405 ms

We will use quick sort algorithm to solve this problem.

```
class Solution {
    public void QuickSort(int[] nums, int low, int high){
        if(low >= high) return;
        

        int low_index=low, high_index=high;
        int pivot = nums[(low+high)/2];

        while(low_index <= high_index){
            while(nums[low_index] < pivot) low_index++;
            while(nums[high_index] > pivot) high_index--;

            if(low_index <= high_index){
                int temp = nums[low_index];
                nums[low_index++] = nums[high_index];
                nums[high_index--] = temp;
            }

        }

        QuickSort(nums, low, low_index-1);
        QuickSort(nums, low_index, high);
    }

    public int[] sortArray(int[] nums) {
        QuickSort(nums, 0, nums.length-1);
        return nums;
    }
}
```

# Solution-2

315 ms

We will use iterative method insted of recursive method. This will reduce the time complexity.

```java
class Solution {

    public int[] sortArray(int[] nums) {
        LinkedList<Integer> intervals = new LinkedList<>();
        intervals.add(0);intervals.add(nums.length-1);
        while(!intervals.isEmpty()){
            int low = intervals.remove();
            int high = intervals.remove();

            if(low >= high) continue;

            int low_index=low, high_index=high;
            int pivot = nums[(high+low)/2];

            while(low_index <= high_index){
                while(nums[low_index] < pivot) low_index++;
                while(nums[high_index] > pivot) high_index--;

                if(low_index <= high_index){
                    int temp = nums[low_index];
                    nums[low_index++] = nums[high_index];
                    nums[high_index--] = temp;
                }

            }

            intervals.add(low);intervals.add(low_index-1);
            intervals.add(low_index);intervals.add(high);
        }


        return nums;
    }
}
```

# Solution-3

128 ms

I will use specialized quick sort algorithm to solve this problem. We will calculate the middle value, before middle value and get average of them. Then we will use this average value as pivot. For example if we have [100,200,300,400,5,600,700,800,900,1000] array, we will calculate the average of 400,300,5 and use it as pivot. If we take 5 as pivot in this situation we will get unbalanced array. This will cause our algorithm work slowly. This apporach will avoid from this situation.

```java
class Solution {

    public int[] sortArray(int[] nums) {
        LinkedList<Integer> intervals = new LinkedList<>();
        intervals.add(0);intervals.add(nums.length-1);
        while(!intervals.isEmpty()){
            int low = intervals.remove();
            int high = intervals.remove();

            if(low >= high) continue;

            int low_index=low, high_index=high;
            int pivot = nums[(high+low)/2];

            while(low_index <= high_index){
                while(nums[low_index] < pivot) low_index++;
                while(nums[high_index] > pivot) high_index--;

                if(low_index <= high_index){
                    int temp = nums[low_index];
                    nums[low_index++] = nums[high_index];
                    nums[high_index--] = temp;
                }

            }

            intervals.add(low);intervals.add(low_index-1);
            intervals.add(low_index);intervals.add(high);
        }


        return nums;
    }
}
```

# Solution-4

124 ms

We will use Merge Sort instead of Quick Sort.

```java
class Solution {
    private void swap(int[] nums, int index1, int index2){
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    }

    private void mergeSort(int[] nums, int low, int high){
        if(low >= high) return;
        if(low == high - 1){
            if(nums[low] > nums[high]) swap(nums, low, high);
        }
        else{
            int mid = (low+high) / 2;
            mergeSort(nums,low, mid-1);
            mergeSort(nums,mid,high);

            int index_left = low, index_right = mid;
            LinkedList<Integer> newArray = new LinkedList<>();
            while(index_left < mid || index_right < high + 1){
                boolean pick_from_left = false, pick_from_right = false;
                if(index_left == mid) pick_from_right = true;
                else if(index_right == high+1) pick_from_left = true;
                else if(nums[index_left] <= nums[index_right]) pick_from_left = true;
                else pick_from_right = true;

                if(pick_from_left){
                    newArray.add(nums[index_left]);
                    index_left += 1;
                }
                else{
                    newArray.add(nums[index_right]);
                    index_right += 1;
                }
            }

            int index = low;
            while(!newArray.isEmpty()) nums[index++] = newArray.remove();
        }
    }

    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1); return nums;
    }
}
```

# Solution-5

42 ms

Tricky Method. We represent every value in the new array. And we count repetiton of numbers in this array. Since we have range of (-510^4, 510^4) this will generate a list that have 10^5 length. This array will use 1.6 MB of Ram.

```java

class Solution {
    int[] reps;
    boolean repsInitialized = false;

    public void initReps(int lowest_value, int highest_value){
        this.reps = new int[highest_value - lowest_value];
        repsInitialized = true;
    }

    public void resetReps(){
        for(int i=0; i<reps.length; i++) reps[i] = 0;
    }

    public int[] sortArray(int[] nums) {
        int lowest_value = (int) (-5 * 10e4);
        int highest_value = (int) (5 * 10e4);
        if(!this.repsInitialized) initReps(lowest_value, highest_value);
        
        resetReps();

        for(int i : nums){
            reps[i - lowest_value]++;
        }

        int index = 0;
        for(int i=0; i<reps.length; i++){
            if(reps[i] != 0){
                for(int j=0; j<reps[i]; j++) nums[index++] = lowest_value + i;
            }
        }

        return nums;
    }
}

```