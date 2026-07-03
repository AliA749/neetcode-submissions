class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character,Character> matched = new HashMap<>();
        matched.put(')','(');
        matched.put(']', '[');
        matched.put('}','{');
        
        for(char i:s.toCharArray()){
            if (matched.containsKey(i)){
                if (!stack.isEmpty() && stack.peek() == matched.get(i)){
                    stack.pop();
                }
                else{
                    return false;
                }
                
            }
            else{
                stack.push(i);
            }
        }
        return stack.isEmpty();

    }
}
