package a1_15211282;
public class MyCharacter {
	// Returns true if ch is a lowercase character ('a' to 'z'); false otherwise.
	public static boolean isLowerCase(char ch) {
		if (ch >='a' && ch <='z')
		return true;
		else
		return false;
		
	}

	// Returns true if ch is an uppercase character ('A' to 'Z'); false otherwise.
	public static boolean isUpperCase(char ch) {
		if(ch >='A' && ch <='Z')
		return true;
		else
		return false;
	}

	// Returns true if ch is a digit ('0' to '9'); false otherwise.
	public static boolean isDigit(char ch) {
		if (ch >='0' && ch <='9')
				return true;
		else
		return false;
	}

	// Returns true if ch is a space (' ') or tab ('\t') character; false otherwise.
	public static boolean isWhitespace(char ch) {
		if (ch =='\t' || ch ==' ')
			return true;
		else
		return false;
	}

	// Returns the lowercase equivalent of ch, if any; otherwise, ch itself is returned.
	public static char toLowerCase(char ch) {
		if(ch >='A' && ch <='Z'){
			return (char)(ch+32);
		}
	else
		return ch;
	}

	// Returns the uppercase equivalent of ch, if any; otherwise, ch itself is returned.
	public static char toUpperCase(char ch) {
			if (ch >='a' && ch <='z')
				return (char)(ch-32);
		return ch;
	}
}
