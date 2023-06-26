# Question

[question link](https://leetcode.com/problems/total-cost-to-hire-k-workers/description/)

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
    For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
    In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.

Return the total cost to hire exactly k workers.

 

Example 1:

    Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
    Output: 11
    Explanation: We hire 3 workers in total. The total cost is initially 0.
    - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
    - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
    - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
    The total hiring cost is 11.

Example 2:

    Input: costs = [1,2,4,1], k = 3, candidates = 3
    Output: 4
    Explanation: We hire 3 workers in total. The total cost is initially 0.
    - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
    - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
    - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
    The total hiring cost is 4.

 

Constraints:

    1 <= costs.length <= 105 
    1 <= costs[i] <= 105
    1 <= k, candidates <= costs.length

# Solution

Time Limit Exceed

```java
import java.util.LinkedList;
class Solution {
    class SortedLinkedList{
        private int size;
        private LinkedList<Integer> linkedList;
        
        public SortedLinkedList(int size){
            this.size = size;
            linkedList = new LinkedList<Integer>();
        }

        public int getFirst() { return linkedList.getFirst();}
        public void removeFirst() {linkedList.removeFirst();}

        public void add(int a){
            int i = 0;
            for(i=0; i<linkedList.size(); i++){
                if(a < linkedList.get(i)) break;
            }
            linkedList.add(i, a);
            if(linkedList.size() > size) linkedList.removeLast();
        }

        public void print(){
            for(int i=0; i<linkedList.size(); i++) System.out.print(linkedList.get(i) + " ");
            System.out.println();
        }

        public int size() {return linkedList.size();}

        public int sum(){
            int sum_ = 0;
            for(int i=0; i<linkedList.size(); i++) sum_ += linkedList.get(i);
            return sum_;
        }
    }

    public long totalCost(int[] costs, int k, int candidates) {
        int left_index = candidates;
        int right_index = costs.length - 1 - candidates;

        if(candidates*2 >= costs.length || right_index <= left_index){
            SortedLinkedList s = new SortedLinkedList(k);
            for(int i=0; i<costs.length;i++) s.add(costs[i]);
            return s.sum();
        }

        SortedLinkedList s_l = new SortedLinkedList(k);
        SortedLinkedList s_r = new SortedLinkedList(k);

        //System.out.println(candidates*2 + " " + (costs.length - (candidates*2)));
        //return 0L;
        ///*
        for(int i=0; i<left_index; i++){
            s_l.add(costs[i]);
        }
        for(int i=right_index+1; i<costs.length; i++){
            s_r.add(costs[i]);
        }

        int sum = 0;
        
        for(int i=0; i<k; i++){
            if(s_l.size() > 0 && s_l.getFirst() <= s_r.getFirst()){
                sum += s_l.getFirst();
                s_l.removeFirst();
                if(right_index >= left_index){
                    s_l.add(costs[left_index]);
                    left_index += 1;
                }
                
            }
            else{
                sum += s_r.getFirst();
                s_r.removeFirst();
                if(right_index >= left_index){
                    s_r.add(costs[right_index]);
                    right_index -= 1;
                }
                
            }
        }
        return sum;
        //*/
    }
}
```

This solution is slow. I try to implement a sorted linked list data structure but every insertion takes O(n) time. And this question requires a lot of insertion and deletion operations.

Instead of Linked List we will use Priority Queue. Priority Queue is not indexed but in this question we don't need indexed. All we need is get smallest element or remove largest element from the queue. So we can use Priority Queue.
Deletion and insertion takes O(logn) time in Priority Queue because it uses binary heap.


#### Solution 2
61 ms
```java
import java.util.PriorityQueue;
class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        int a=0, b=costs.length-1;
        PriorityQueue<Integer> leftQ = new PriorityQueue<>();
        PriorityQueue<Integer> rightQ = new PriorityQueue<>();
            
        while(leftQ.size() < candidates) leftQ.offer(costs[a++]);
        while(b >= a && rightQ.size() < candidates) rightQ.offer(costs[b--]);

        long res = 0;
        for(int i=0; i<k; i++){
            
            if(leftQ.size() > 0 && 
            (rightQ.size() == 0 || leftQ.peek() <= rightQ.peek())
            ){
                res += leftQ.poll();
                if(b >= a) leftQ.offer(costs[a++]);
            }
            else{
                res += rightQ.poll();
                if(b >= a) rightQ.offer(costs[b--]);
            }
        }
        return res;
    }
}
```

We create two priority queues. One for left side and one for right side. We check every time which side has smaller element and we add that element to the sum. And we add next element from that side to the queue. We do this k times.