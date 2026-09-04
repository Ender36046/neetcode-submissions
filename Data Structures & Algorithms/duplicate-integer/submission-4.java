
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> numCount = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(numCount.containsKey(nums[i])){
                return true;
            }else{
                numCount.add(nums[i]);
            }
        }
        return false;
    }
}