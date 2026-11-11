
import java.util.ArrayDeque;
import java.util.Deque;

public class EvaluateReversePolishNotation {

    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        int a, b;

        for (String token : tokens) {
            switch (token) {
                case "/" -> {
                    a = stack.pop();
                    b = stack.pop();
                    if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
                        stack.push(-(Math.abs(b) / Math.abs(a)));
                    } else {
                        stack.push((Math.abs(b) / Math.abs(a)));
                    }
                }
                case "*" -> {
                    a = stack.pop();
                    b = stack.pop();
                    stack.push(a * b);
                }
                case "-" -> {
                    a = stack.pop();
                    b = stack.pop();
                    stack.push(a - b);
                }
                case "+" -> {
                    a = stack.pop();
                    b = stack.pop();
                    stack.push(a + b);
                }
                default ->
                    stack.push(Integer.valueOf(token));
            }
        }
        return stack.pop();
    }

    public static void main(String[] args) {
        EvaluateReversePolishNotation solution = new EvaluateReversePolishNotation();
        String[] tokens = new String[]{"4", "13", "5", "/", "+"};

        solution.evalRPN(tokens);
    }
}
