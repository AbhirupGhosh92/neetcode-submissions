class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lp = 0;
        int rp = numbers.length - 1;
        int[] answer = new int[0];
        while(lp < rp){
            if (numbers[lp] + numbers[rp] > target){
                rp -= 1;
            }
            else if (numbers[lp] + numbers[rp] < target){
                lp += 1;
            }
            else{
                answer =  new int[]{lp+1,rp+1};
                break;
            }
        }
        return answer;
    }
}
