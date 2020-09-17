import java.util.Hashtable;

public class longestSubstring {

	public static void main(String[] args) {
		String in1 = "abcabcbb";
		String in2 = "bbbbb";
		String in3 = "pwwkew";

		System.out.println(longSubString(in3));
	}

	public static int longSubString(String input) {
		if (input == "" || input == null) {
			return 0;
		}

		int prevLen = 0;
		int currLen = 0;
		Hashtable<String, Integer> hash = new Hashtable<String, Integer>();

		for (int i = 0; i < input.length(); i++) {
			String c = input.substring(i, i + 1);
			if (!hash.containsKey(c)) {
				hash.put(c, 1);
				currLen++;
			} else {
				prevLen = Math.max(prevLen, currLen);
				currLen = 1;
				hash.clear();
				hash.put(c, 1);
			}
		}

		return prevLen;
	}

}
