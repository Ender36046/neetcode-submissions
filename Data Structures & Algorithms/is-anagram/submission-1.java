class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> charCount1 = new HashMap<>();
        HashMap<Character, Integer> charCount2 = new HashMap<>();
        for(int i =0; i < s.length(); i++){
            char currentChar1 = s.charAt(i);
            charCount1.merge(currentChar1, 1, (oldVal,newVal) -> oldVal+newVal);
        }
        for(int j =0; j< t.length(); j++){
            char currentChar2 = t.charAt(j);
            charCount2.merge(currentChar2, 1, (oldVal,newVal) -> oldVal + newVal);
        }
        return charCount1.equals(charCount2);
    }
}
