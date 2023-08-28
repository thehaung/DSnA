package vn.leetcode.linkedlist;

import java.util.LinkedList;
import java.util.List;

// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
public class LetterCombinations {

    public List<String> letterCombinations(String digits) {
        LinkedList<String> ans = new LinkedList<>();
        if (digits.isEmpty()) return ans;
        ans.offer("");

        String[] strMapping = new String[]{"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        for (int i = 0; i < digits.length(); i++) {
            int index = Character.getNumericValue(digits.charAt(i));
            while (ans.peek() != null && ans.peek().length() == i) {
                String t = ans.remove();
                for (char s : strMapping[index].toCharArray()) {
                    ans.add(t + s);
                }
            }
        }
        return ans;
    }
    // Time Complexity: O(4^N)
    // Space Complexity: O(4^N)
    // 4 is the maximum digits mapping characters

    public static void main(String[] args) {
        LetterCombinations letterCombinations = new LetterCombinations();
        System.out.println(letterCombinations.letterCombinations("23"));
    }
}
