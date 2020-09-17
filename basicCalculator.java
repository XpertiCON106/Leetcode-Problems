import java.util.LinkedList;
import java.util.Queue;

public class basicCalculator {
	public static void main(String[] args) {
		String cal1 = "1+1";
		String cal2 = "2-1+2";
		String cal3 = "2*1+8";
		String cal4 = "2*5/1+3";
		System.out.println(calculate(cal2));
	}

	public static int calculate(String input) {
		Queue<Integer> nums = new LinkedList<>();
		Queue<String> ops = new LinkedList<>();
		String c = "";
		for (int i = 0; i < input.length(); i++) {
			if (input.substring(i, i + 1).equals("+")
					|| input.substring(i, i + 1).equals("-")
					|| input.substring(i, i + 1).equals("/")
					|| input.substring(i, i + 1).equals("*")) {

				if (c != "") {
					nums.add(Integer.parseInt(c));
					c = "";
				}
				ops.add(input.substring(i, i + 1));
			} else {
				c += input.substring(i, i + 1);
			}
		}
		nums.add(Integer.parseInt(c));
		int num1 = nums.remove();
		int num2 = 0;
		while (ops.size() > 0) {
			String ops1 = ops.remove();
			num2 = nums.remove();
			if (ops1.equals("+")) {	num1 = num1 + num2;}
			if (ops1.equals("-")) { num1 = num1 - num2;}
			if (ops1.equals("*")) { num1 = num1 * num2;}
			if (ops1.equals("/")) { num1 = num1 / num2;}
		}
		return num1;
	}
}
