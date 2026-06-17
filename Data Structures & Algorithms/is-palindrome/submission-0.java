class Solution {
    public boolean isPalindrome(String s) {
        String temp = "";
        String input = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        for (int i = input.length()-1 ; i >= 0 ; i --){
            
               temp += input.charAt(i);
        }
        System.out.println(input);
        return temp.equals(input);
    }
}
