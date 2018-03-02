package a1_15211282;
public class MyString {
	// Returns a new string with the characters in str converted to lowercase.
	public static String toLowerCase(String str) {
		String str1="";
		for(int i =0; i < str.length(); i ++){
			
			char ch=MyCharacter.toLowerCase(str.charAt(i));
			str1 += ch;
			
		}
		return str1;
	}

	// Returns a new string with the characters in str converted to uppercase.
	public static String toUpperCase(String str) {
		String str1="";
		for(int i =0; i < str.length(); i ++){
			
			char ch=MyCharacter.toUpperCase(str.charAt(i));
			str1 += ch;
			
		}
		return str1;
	}

	// Returns true if the two strings s1 and s2 are equal; false otherwise. 
	// Two strings are considered equal if they are of the same length and 
	// corresponding characters in the two strings are equal.
	public static boolean equals(String s1, String s2) {
		if (s1.length() == s2.length()){
			for (int i=0; i < s1.length(); i++){
				if (s1.charAt(i) != s2.charAt(i))
					return false;
			}
				return true;
		}
		else
		return false;
	}
	
	// Returns true if the two strings s1 and s2 are equal ignoring case; false 
	// otherwise. Two strings are considered equal if they are of the same length 
	// and corresponding characters in the two strings are equal ignoring case.
	public static boolean equalsIgnoreCase(String s1, String s2) {
		
		s1=toLowerCase(s1);
		s2=toLowerCase(s2);
		return MyString.equals(s1, s2);
	}

	// Returns a new string with every occurrence of character ch1 in str replaced 
	// with character ch2.	
	public static String replace(String str, char ch1, char ch2) {
		String str1 = "";
		char ch;
		for (int i=0; i < str.length(); i++){
			ch=str.charAt(i);
			if (ch==ch1)
				ch=ch2;
			str1 +=ch;
		}
		return str1;
	}

	// Returns a new string with all leading and trailing whitespace characters (space 
	// or tab characters) in str removed.
	public static String trim(String str) {
		String str1 = "";
		int start = 0;
		int end = str.length();
		while(start < end && MyCharacter.isWhitespace(str.charAt(start))){
			start++;
		}
		while(start < end && MyCharacter.isWhitespace(str.charAt(end - 1))){
			end--;
		}
		if((start > 0) || (end < str.length())){
			for(int i = start; i < end;i++){
				str1 += str.charAt(i);
			}
			return str1;
		}
		else{
			return str;
		}
	}
	
	// Returns true if str starts with the specified prefix; false otherwise.
	public static boolean startsWith(String str, String prefix) {
		String common="";
		if(str.length()>=prefix.length()){
		for(int i =0; i<=(prefix.length()-1);i++){
			if (str.charAt(i)==prefix.charAt(i))
				common+=prefix.charAt(i);
			else
				break;
		}
         return MyString.equals(common, prefix);
		}
         else
        	 return false;
	}

	// Returns true if str ends with the specified suffix; false otherwise.
	public static boolean endsWith(String str, String suffix) {
		String common="";
		if ( str.length() >= suffix.length()){
			int a=str.length()-suffix.length();
			for(int i=a;i<str.length();i++){
				common+=str.charAt(i);
			}
			return MyString.equals(common,suffix);
			}
		else
			return false;
	}
	}

