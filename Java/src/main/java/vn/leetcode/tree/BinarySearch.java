package vn.leetcode.tree;

import java.util.stream.Stream;

public class BinarySearch {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
                left++;
            if (nums[mid] > target)
                right--;
            if (nums[mid] == target)
                return mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch binarySearch = new BinarySearch();
        System.out.println(binarySearch.search(Stream.of(-1,0,3,5,9,12).mapToInt(Integer::intValue).toArray(), 9));
    }
}
