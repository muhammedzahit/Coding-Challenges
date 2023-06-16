# Question

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character ([More info](https://en.wikipedia.org/wiki/Lexicographic_order)).

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.

# Solution

Runtime : 1 ms

```java
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;

class Solution {
    // This function check that word1 lexigraphically before than word2
    // If not returns False
    private boolean isSortedLexigraphically(String word1, String word2, Dictionary<Character, Integer> dict){
        int word1Length = word1.length();
        int word2Length = word2.length();
        int minLength = Math.min(word1Length, word2Length);

        for(int i=0; i<minLength; i++){
            int char1_index = dict.get(word1.charAt(i));
            int char2_index = dict.get(word2.charAt(i));
            if(char1_index < char2_index) return true;
            else if(char1_index > char2_index) return false;
        }

        // because of empty string lexigraphically before than any other characters
        // smaller word must be before than other word
        if(word1Length <= word2Length) return true;
        return false;
    }
    
    public boolean isAlienSorted(String[] words, String order) {
        Dictionary<Character, Integer> dict = new Hashtable<>();

        // store every char in dictionary recording to given order
        for(int i=0; i<order.length(); i++){
            dict.put(order.charAt(i), i);
        }

        // check every pair of words
        for(int i=0; i<words.length - 1; i++){
            if(!isSortedLexigraphically(words[i], words[i+1], dict)){
                return false;
            }
        }

        return true;
    }
}
```

Create a dictionary to store every character in given order. Then check every pair of words. If the first word is not lexigraphically before than the second word, return false. If all pairs are lexigraphically sorted, return true.