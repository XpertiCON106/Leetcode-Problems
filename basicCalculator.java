import java.util.LinkedList;
import java.util.Queue;
/*
So for this problem I decided to employ a queue.
Basically, I have two queues; one for the numbers and the one for the operations.
In the first part, I fill out the respective queues.
Then, I have a while loop that goes through the operations one by one in the queue and gets 2 numbers to do the operations with.
I have one number, num1, that I change throughout the operation.
Once we have no more operation to do, we know we have the answer which has been changing throughout, so I return that.

One issue I had was not adding in the last integer in the string input. I fixed this by adding the last character that my string collects. This makes sure we are adding the last integer from our input.

I have one for loop that goes through the input once. I have another loop that goes through the operations queue once. So, overall runtime is linear, O(n).
*/
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
