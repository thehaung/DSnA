package vn.leetcode.array;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

// https://leetcode.com/problems/valid-anagram/
public class IsAnagram {

    public boolean isAnagram(String s, String t) {
        return v2(s, t);
    }

    public boolean v1(String s, String t) {
        if (s.length() != t.length())
            return false;

        Map<Character, Integer> sMap = new HashMap<>();
        for (char str : s.toCharArray()) {
            sMap.put(str, sMap.getOrDefault(str, 0) + 1);
        }
        Map<Character, Integer> tMap = new HashMap<>();
        for (char str : t.toCharArray()) {
            tMap.put(str, tMap.getOrDefault(str, 0) + 1);
        }

        for (Map.Entry<Character, Integer> entry : sMap.entrySet()) {
            if (!Objects.equals(tMap.getOrDefault(entry.getKey(), 0), entry.getValue()))
                return false;
        }
        return true;
    }

    /*
     Idea khởi tạo 1 bucket với length là 26 (26 chữ cái)
     Khi loop qua mỗi chữ cái có trong String
     Đối với mỗi String ta sẽ - 'a' để lấy index của nó trong bucket
     Với String s ta sẽ ++ giá trị trong bucket
     Với String t ta sẽ -- giá trị trong bucket
     Cuối cùng loop hết bucket nếu giá trị != 0 nghĩa là String ở s hoặc t bị dư -> violate
     */
    public boolean v2(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++)
            alphabet[s.charAt(i) - 'a']++;

        for (int i = 0; i < t.length(); i++)
            alphabet[t.charAt(i) - 'a']--;

        for (int i : alphabet)
            if (i != 0)
                return false;
        return true;
    }
    // Time Complexity: O(N)
    // Space Complexity: O(26)

    public static void main(String[] args) {

        IsAnagram isAnagram = new IsAnagram();
        System.out.println(isAnagram.isAnagram("cat", "tac"));
    }
}
