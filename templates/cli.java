/* Java CLI Template Program
 * @author [AUTHOR]
 * Created: [DATE]
 * Updated: [DATE]
 * Description: [DESCRIPTION]
 */

// This part is used for https://github.com/hussein-esmail7/template-maker
// templateDescription: Java CLI Template

import java.util.Arrays;
import java.util.Scanner; // Import the Scanner class for user input

import java.util.List;

public class cli {

	/**
	 * @param args
	 */
	final static String COMMAND_EXIT = "exit";                                              // This is the command to exit the program
	final static String COMMAND_HELP = "help";                                              // This is the command to get to the help message
	final static String STR_INTRO = "CLI Template Program";                                 // This is printed at the beginning of every program run
	final static String STR_INPUT = "> ";                                                   // This is the input character each time they are able to type a new command
	final static String STR_INVALID = "Invalid command!";                                   // This is printed when the user types something that the program does not recignize 
	final static String STR_PROGRAM_EXITED = "Program exited.";
	final static String STR_HELP = "===== CLI Template program ====="
			+ "\n" + COMMAND_EXIT
			+ "\n\tExit the program."
			+ "\n" + COMMAND_HELP
            + "\n\tHelp command (this one)."
            + "\n===== CLI Template program =====";
	
	public static void main(String[] args) {
		System.out.println(STR_INTRO);
		while (true) {                                                                      // Keep asking for commands until 
			String[] user_input = input(STR_INPUT).split(" ");				                // Ask for the user input and split it into a String[]
            if (user_input.length == 1 && user_input[0].equals(COMMAND_EXIT)) {             // If the user types the exit command
                System.out.println(STR_PROGRAM_EXITED);
                System.exit(0);                                                             // Exit the program
            } else if (user_input.length == 1 && user_input[0].contains(COMMAND_HELP)) {    // If the user types the help command
                System.out.println(STR_HELP);                                               // Print the help message
            } else {                                                                        // More commands can be put above here
                if (!user_input[0].equals("") && user_input.length != 1) {                  // If the first entry is not an empty string
                    System.out.println(STR_INVALID);                                        // Print that the most recent command was invalid
                }                                                                           // Else: Do nothing, go to the next input line
            }
	}
    }
    
    public static String input(String ask) {
	    Scanner scanner = new Scanner(System.in);  							                // Create a Scanner object
	    System.out.print(ask);												                // Print the string before input (most cases "> ")
	    return scanner.nextLine();  										                // Return the user input
	}

}
