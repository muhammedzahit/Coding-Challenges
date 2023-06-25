# Question

[question link](https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/)

On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

    Input: n = 6, delay = 2, forget = 4
    Output: 5
    Explanation:
    Day 1: Suppose the first person is named A. (1 person)
    Day 2: A is the only person who knows the secret. (1 person)
    Day 3: A shares the secret with a new person, B. (2 people)
    Day 4: A shares the secret with a new person, C. (3 people)
    Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
    Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

Example 2:

    Input: n = 4, delay = 1, forget = 3
    Output: 6
    Explanation:
    Day 1: The first person is named A. (1 person)
    Day 2: A shares the secret with B. (2 people)
    Day 3: A and B share the secret with 2 new people, C and D. (4 people)
    Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)

 

Constraints:

    2 <= n <= 1000
    1 <= delay < forget <= n

# Solution

4 ms

```java
class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        long share = 0; // Person will share
        long[] dp = new long[n+1];
        dp[1] = 1; // 1 person found the secret

        long mod = (long) 1e9 + 7;

        for(int i=2; i<=n; i++){
            int delay_index = Math.max(i-delay, 0);
            int forget_index = Math.max(i-forget, 0);
            dp[i] = share + dp[delay_index] - dp[forget_index];
            dp[i] = (dp[i] + mod) %  mod;
            share = dp[i];
        }

        long res = 0;
        for(int i=n; i>n-forget; i--){
            res = (res + dp[i]) % mod;
        }
        return (int) ((res + mod) % (mod));

    }
}
```

dp[i] means the number of people who found the secret on day i.
share means the number of people who will share the secret on day i.
dp[i] = share + dp[delay_index] - dp[forget_index];

- dp[delay_index] : the number of people who found the secret on day delay_index, they will share the secret on day i and stop sharing the secret on day i + forget.

- dp[forget_index] : the number of people who found the secret on day forget_index, they will stop sharing the secret on day i.

We simply adding new sharers and removing people that forget the secret. And store the current number of people that sharing secret in secret variable.

Finally, we need to sum up the number of people that found the secret on the last forget days.