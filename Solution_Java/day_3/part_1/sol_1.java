import java.io.*;
import java.util.regex.*;

public class sol_1 {
    // Variable to hold the sum of all multiplication results
    private static int totalSum = 0;

    public static void main(String[] args) {
        String input = "";

        // Read the input file
        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            String line;
            while ((line = reader.readLine()) != null) {
                input += line + "\n"; // Concatenate lines into a single string
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Could not open file");
            e.printStackTrace();
            return;
        }

        // Call method to find the mul patterns
        int patternCount = findMulPattern(input);

        // Output the result
        System.out.println("Number of patterns found: " + patternCount);
        System.out.println("Final Sum = " + totalSum);
    }

    // Method to find and process the mul(number,number) patterns
    public static int findMulPattern(String str) {
        // Regex pattern for mul(number,number)
        String pattern = "mul\\((\\d+),(\\d+)\\)";

        // Create a Pattern object
        Pattern compiledPattern = Pattern.compile(pattern);
        Matcher matcher = compiledPattern.matcher(str);

        int patternCount = 0;

        // Find all matches
        while (matcher.find()) {
            // Extract the numbers
            int number1 = Integer.parseInt(matcher.group(1));
            int number2 = Integer.parseInt(matcher.group(2));

            // Print the found pattern
            System.out.println("Found pattern: mul(" + number1 + "," + number2 + ")");

            // Add the product of the numbers to the total sum
            totalSum += (number1 * number2);

            // Increment the pattern count
            patternCount++;
        }

        return patternCount;
    }
}