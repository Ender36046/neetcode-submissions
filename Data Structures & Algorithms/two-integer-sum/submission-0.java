class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if(numMap.containsKey(difference)){
                int arr[] = {i, numMap.get(difference)};
                Arrays.sort(arr);
                return arr;
            }else{
                numMap.put(nums[i],i);
            }
        }
        int arr[] ={-1,-1};
        return arr;
    }
}
