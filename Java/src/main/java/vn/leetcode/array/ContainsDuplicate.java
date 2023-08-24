package vn.leetcode.array;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

// https://leetcode.com/problems/contains-duplicate
public class ContainsDuplicate {

    public boolean containsDuplicate(List<Integer> nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            if (!numsSet.add(num))
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        ContainsDuplicate containsDuplicate = new ContainsDuplicate();
        System.out.println(containsDuplicate.containsDuplicate(List.of(1, 2, 3)));
    }
}
