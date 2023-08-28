package vn.leetcode.tree;

import java.util.List;

public class FindIndexOfSortedNums {

    public int findIndexOfSortedNums(int[] nums, int num) {
        var left = 0;
        var right = nums.length - 1;

        while (left <= right) {
            var mid = (left + right) / 2;
            if (num == nums[mid]) {
                return mid;
            } else if (num > nums[mid]) {
                left++;
            } else {
                right--;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        FindIndexOfSortedNums indexOfSortedNums = new FindIndexOfSortedNums();
        List<Integer> nums = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        System.out.println(indexOfSortedNums.findIndexOfSortedNums(nums.stream().mapToInt(Integer::intValue).toArray(), 8));
    }
}
