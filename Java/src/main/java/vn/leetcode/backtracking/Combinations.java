package vn.leetcode.backtracking;

import java.util.ArrayList;
import java.util.List;

public class Combinations {

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), n, k, 1);
        return res;
    }

    private void backtrack(List<List<Integer>> res, List<Integer> curr, int n, int k, int num) {
        if (curr.size() == k) {
            res.add(new ArrayList<>(curr));
            return;
        }

        for (int i = num; i <= n; i++) {
            curr.add(i);
            backtrack(res, curr, n, k, i + 1);
            curr.remove(curr.size() - 1);
        }
    }


    public static void main(String[] args) {
        Combinations combinations = new Combinations();
        System.out.println(combinations.combine(4, 2));
    }
}
