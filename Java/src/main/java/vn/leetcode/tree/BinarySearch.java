package vn.leetcode.tree;

import java.util.stream.Stream;

public class BinarySearch {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;

        while (left <= right) {
            mid = (right - left) / 2 + left;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch binarySearch = new BinarySearch();
        System.out.println(binarySearch.search(Stream.of(-1, 0, 3, 5, 9, 12).mapToInt(Integer::intValue).toArray(), 9));
    }
}
