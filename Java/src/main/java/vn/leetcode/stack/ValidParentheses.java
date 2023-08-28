package vn.leetcode.stack;

import java.util.ArrayDeque;
import java.util.Map;

public class ValidParentheses {

    private boolean isValid(String s) {
        var stack = new ArrayDeque<String>();
        var matchingPair = Map.of(
                ")", "(",
                "}", "{",
                "]", "["
        );

        for (Character ch : s.toCharArray()) {
            if ("({[".contains(ch.toString())) {
                stack.add(ch.toString());
                continue;
            }

            if (stack.isEmpty() || !stack.pop().equals(matchingPair.getOrDefault(ch.toString(), "")))
                return false;
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        ValidParentheses validParentheses = new ValidParentheses();
        System.out.println(validParentheses.isValid("()[]{}"));
    }
}
