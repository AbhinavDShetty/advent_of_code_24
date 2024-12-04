import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class ListDistanceFromFile {

    public static int totalDistance(int[] leftList, int[] rightList) {
        // Sort both lists
        Arrays.sort(leftList);
        Arrays.sort(rightList);
        
        // Calculate the total distance by summing the absolute differences of each pair
        int total = 0;
        for (int i = 0; i < leftList.length; i++) {
            total += Math.abs(leftList[i] - rightList[i]);
        }
        
        return total;
    }

    public static void main(String[] args) {
        try {
            // Read input from file "input.txt"
            File file = new File("input.txt");
            Scanner scanner = new Scanner(file);
            
            // Initialize arrays to hold the input
            int[] leftList = new int[1001];
            int[] rightList = new int[1001];
            int index = 0;
            
            // Read data into arrays
            while (scanner.hasNext()) {
                leftList[index] = scanner.nextInt();
                rightList[index] = scanner.nextInt();
                index++;
            }
            
            // Close scanner
            scanner.close();
            
            // Compute the total distance
            int result = totalDistance(leftList, rightList);
            
            // Output the result
            System.out.println(result);  // Output: 11
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }
}
