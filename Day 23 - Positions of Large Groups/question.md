# Question

[Question Link](https://leetcode.com/problems/positions-of-large-groups/)

In a string `s` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `s = "abbxxxxzyy"` has the groups `"a"`, `"bb"`, `"xxxx"`, `"z"`, and `"yy"`.

A group is identified by an interval `[start, end]`, where `start` and `end` denote the start and end indices (inclusive) of the group. In the above example, `"xxxx"` has the interval `[3,6]`.

A group is considered **large** if it has 3 or more characters.

Return *the intervals of every **large** group sorted in **increasing order by start index***.

**Example 1:**

```
Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
```

**Example 2:**

```
Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
```

**Example 3:**

```
Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
```

# Solution

3 ms

```java
class Solution {
    class Group{
        List<Integer> intervals;
        int size;
        
        public Group(int interval1, int interval2){
            intervals = new ArrayList<>();
            intervals.add(interval1);
            intervals.add(interval2);
            size = interval2 - interval1;
        }
    }

    class GroupComparator implements Comparator<Group>{
        @Override
        public int compare(Group grp1, Group grp2){
            return grp1.size > grp2.size ? 1 : 0;
        }
    }
    
    public List<List<Integer>> largeGroupPositions(String s) {
        List<Group> groups = new ArrayList<>();
        char before = s.charAt(0);
        int beforeIndex = 0;
        int i=1;
        for(i=1; i<s.length(); i++){
            if(s.charAt(i) == before) continue;

            if(i-1 - beforeIndex >= 2)  groups.add(new Group(beforeIndex, i-1));
            beforeIndex = i; before = s.charAt(i);
        }
        
        if(i-1 - beforeIndex >= 2)  groups.add(new Group(beforeIndex, i-1));

        //Collections.sort(groups, new GroupComparator());
        List<List<Integer>> res = new ArrayList<>();
        for(Group grp : groups){
            List<Integer> add_ = new ArrayList<>();
            add_.add(grp.intervals.get(0));
            add_.add(grp.intervals.get(1));
            res.add(add_);
            //System.out.println(grp.intervals.get(0) + " " + grp.intervals.get(1));
        }


        return res;
    }
}
```

In this solution, I used `Group` class to store the interval of each group and its size. And I used `GroupComparator` class to sort the groups by its size. But it was not necessary to sort the groups. So I commented out the sorting part. But if problem requires to sort the groups, then you can use `GroupComparator` class.