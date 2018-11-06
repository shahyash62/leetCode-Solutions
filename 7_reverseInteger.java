class Solution {
    public int reverse(int x) {
        int rx = 0;
        int multiplier = 10;
        boolean flag = false;
        if (x < 0) {
            flag = true;
            x = Math.abs(x);
        }
        for (;x > 0; x /= 10) {
            try {
                rx = Math.addExact(Math.multiplyExact(rx,multiplier),(x%10));
            } catch (ArithmeticException e) {
                return 0;
            }
        }
        if (flag)
            return -rx;
        else
            return rx;
    }
}
