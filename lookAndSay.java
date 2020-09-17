import java.util.ArrayList;

/*
Question:
Given an array of integers, procure its Look-and-Say Sequence.
A Look-and-Say Sequence is how you would describe the array out loud, saying how many of each value appears.
*/
public class Look_and_Say {

	public static void main(String[] args) {
		int[] arr1 = { 1, 1, 2, 1 };
		int[] arr2 = { 2, 1, 1, 2, 1, 1 };
		int[] arr3 = { 1, 2, 2, 1, 1, 2, 2, 1 };
		int[] arr4 = { 1, 1, 2, 2, 2, 1, 2, 2, 1, 1 };
		int[] arr5 = { 2 };

		for (int x : las(arr5)) {
			System.out.println(x);
		}
	}

	/*
	 * My approach was to go through all the elements in the array and keep track of the previous
	 * number. There is a counter that checks how many times the previous number appears
	 * in the next sequence of numbers. Once its different, the counter is reseted and added into the arraylist.
	 * The next previous number is this current one and the for loop continues;
	 *
	 * The time complexity of the program in O(n) because the program runs through the array once.
	 *
	 * One issue I had was the for loop would disregard the last element. I fixed the issue by
	 * including additional statements that includes the last counter and previous number.
	 * that seems to have fixed the problem.
	 */

	public static ArrayList<Integer> las(int[] input) {
		if (input == null) {
			return null;
		}
		if (input.length == 0) {
			return new ArrayList<Integer>();
		}
		ArrayList<Integer> result = new ArrayList<Integer>();
		int counter = 1;
		int prevNumber = input[0];
		for (int i = 1; i < input.length; i++) {
			if (input[i] != prevNumber) {
				result.add(counter);
				result.add(prevNumber);
				counter = 1;
				prevNumber = input[i];
			} else {
				counter++;
			}
		}
		result.add(counter);
		result.add(prevNumber);

		return result;
	}

}
