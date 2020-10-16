/** Java CLI Template Program
 * @author Hussein Esmail
 * Created: 2020 08 28
 * Updated: 2020 08 28
 * Description: This program is a skeleton template for an infinite-input program
 */


import java.util.Arrays;
import java.util.Scanner; // Import the Scanner class for user input

import java.util.List;

public class cli {

	/**
	 * @param args
	 */
	String str_intro = "Opendir program";
	final static String COMMAND_EXIT = "exit";
	final static String COMMAND_HELP = "help";
	static String str_input = "> ";
	static String str_split = " ";
	static String str_invalid_command = "Invalid command!";
	static String str_help = "CLI Template program"
			+ "\n" + command_exit
			+ "\n\tExit the program."
			+ "\n" + command_help
			+ "\n\tHelp command (this one).";
	
	
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); // Create a Scanner object
		while (true) { // Keep asking for commands until 
			System.out.print(str_input); // Input character
		    String[] user_input_unformatted = scanner.nextLine().split(str_split);  // Read user input
		    List<String> user_input = Arrays.asList(user_input_unformatted);
	    	System.out.println(user_input.size());
		    if (user_input.size() == 1 && user_input[0].equals(COMMAND_EXIT)) { // Exit the program
	    		scanner.close();
	    	    System.exit(0);
	    	} else if (user_input.size() == 1 && user_input.contains(COMMAND_HELP)) {
	    		System.out.println(str_help);
	    		// More commands below here but above the else{} statement
	    	} else {
	    		if (!user_input.get(0).equals("")) { // If the first entry is not an empty string
	    			System.out.println(str_invalid_command);
	    		} // Else: Do nothing
	    	}
		}
	}

}
