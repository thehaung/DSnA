package vn.leetcode.backtracking;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
public class LetterCombinations {

    // Version 2 use backtracking instead DFS LL
    private final Map<Character, String> digitMapping = Map.of(
            '2',
            "abc",
            '3',
            "def",
            '4',
            "ghi",
            '5',
            "jkl",
            '6',
            "mno",
            '7',
            "pqrs",
            '8',
            "tuv",
            '9',
            "wxyz"
    );

    private List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return new ArrayList<>();
        }

        List<String> ans = new ArrayList<>();
        String cur = "";
        backtrack(digits, ans, cur, 0);
        return ans;
    }

    private void backtrack(String digits, List<String> ans, String cur, int index) {
        if (cur.length() == digits.length()) ans.add(cur);
        if (index < digits.length()) {
            String digit = digitMapping.get(digits.charAt(index));
            for (char c : digit.toCharArray()) {
                backtrack(digits, ans, cur + c, index + 1);
            }
        }
    }

    public static void main(String[] args) {
        LetterCombinations letterCombinations = new LetterCombinations();
        System.out.println(letterCombinations.letterCombinations("23"));
    }
}
