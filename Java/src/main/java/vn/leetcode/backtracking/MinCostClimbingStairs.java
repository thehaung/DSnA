package vn.leetcode.backtracking;

import java.util.stream.Stream;

public class MinCostClimbingStairs {
    private Integer[] cache;
    private int[] cost;

    public int minCostClimbingStairs(int[] cost) {
        return this.v2CalcViaLoop(cost);
    }

    private int v1Recursion(int[] cost) {
        this.cost = cost;
        this.cache = new Integer[cost.length];

        int startIndex0 = recursion(0);
        int startIndex1 = recursion(1);
        return Math.min(startIndex0, startIndex1);
    }

    private int recursion(int index) {
        // Base Case
        if (index >= cost.length) return 0;
        if (cache[index] != null) return cache[index];

        int take1Step = recursion(index + 1);
        int take2Step = recursion(index + 2);
        cache[index] = Math.min(take1Step, take2Step) + cost[index];
        return cache[index];
    }

    private int v2CalcViaLoop(int[] cost) {
        int p1 = 0;
        int p2 = 0;
        for (int i = 2; i <= cost.length; i++) {
            int tempMinCost = Math.min(p1 + cost[i - 2], p2 + cost[i - 1]);
            p1 = p2;
            p2 = tempMinCost;
        }
        return p2;
    }

    public static void main(String[] args) {
        MinCostClimbingStairs minCostClimbingStairs = new MinCostClimbingStairs();
        System.out.println(minCostClimbingStairs.minCostClimbingStairs(Stream.of(10, 15, 20).mapToInt(Integer::intValue).toArray()));
    }
}
