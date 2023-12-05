package vn.leetcode.array;

import java.util.stream.Stream;

public class SellStock {

    public int calcProfit(int[] prices) {
        int lowestPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int currPrice : prices) {
            if (currPrice - lowestPrice > maxProfit)
                maxProfit = currPrice - lowestPrice;

            if (currPrice < lowestPrice)
                lowestPrice = currPrice;
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        Integer nums = 10;
        String valueStr = String.valueOf(nums);



    }
}
