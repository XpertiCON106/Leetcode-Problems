import java.util.Hashtable;
/*
For this problem, I employed a hashtable.
Basically go through the characters of the entire string and put them in the hashtable.
Also keep track of how many characters we are putting in.
As soon as the next character is already in the hash,
we clear the hash, decided if the current length is smaller or bigger than
the previous length and change accordingly. And then we reset the current length
and continue with the string. This makes sure we are going through the entire array
only once and since we are using a hashtable, our containsKey() methods runtime is O(1).

So overall runtime of the program is O(n).

One issue I was having was not including the next character that’s found on the hash table.
I fixed this by immediately putting the next character that was already in the hash into the new hash table.  

*/
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
