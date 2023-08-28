# Question

[Question Link](https://leetcode.com/problems/make-the-string-great/description/)

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

    Input: s = "leEeetcode"
    Output: "leetcode"
    Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:

    Input: s = "abBAcC"
    Output: ""
    Explanation: We have many possible scenarios, and all lead to the same answer. For example:
    "abBAcC" --> "aAcC" --> "cC" --> ""
    "abBAcC" --> "abBA" --> "aA" --> ""

Example 3:

    Input: s = "s"
    Output: "s"

 

Constraints:

    1 <= s.length <= 100
    s contains only lower and upper case English letters.

# Solution

```java
class Solution {
    public String makeGood(String s) {
        ArrayList<Character> chars = new ArrayList<>();
        for(int i=0; i<s.length(); i++){
            Character curr = s.charAt(i);
            if(chars.size() == 0) chars.add(curr);
            else{
                Character last = chars.get(chars.size() - 1);
                Character lowercaseCurr = Character.toLowerCase(curr);
                Character lowercaseLast = Character.toLowerCase(last);
                if(last != curr && (lowercaseCurr == lowercaseLast))
                    chars.remove(chars.size() - 1);
                else
                    chars.add(curr);
            }
        }
        String res = "";
        for(int i=0; i<chars.size(); i++) res += chars.get(i);
        return res;
    }
}
```

Runtime : 3ms
Memory : 41.66mb

In this solution, we use an ArrayList to store the characters of the string. We iterate through the string and compare the current character to the last character in the ArrayList. If the current character is the same as the last character but in a different case, we remove the last character from the ArrayList. Otherwise, we add the current character to the ArrayList. Finally, we convert the ArrayList to a string and return it.