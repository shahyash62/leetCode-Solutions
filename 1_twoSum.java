class Solution {
    public int[] twoSum(int[] nums, int target) {
        int arrayLength = nums.length;
        int soln[] = new int[2];
        LOOP:
        for (int i = 0; i < arrayLength; i++) {
            for(int j = 0; j < arrayLength; j++) {
                if(i == j)
                    continue;
                if((nums[i] + nums[j])==target) {
                    soln[0] = i; soln[1] = j;
                    break LOOP;
                }
            }
        }
        return soln;
    }
}
