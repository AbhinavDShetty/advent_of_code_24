import java.io.*;
import java.util.*;

public class Sol_3 {
    public static void main(String[] args) {
        String[] input = new String[250];
        int lineCount = 0;
        int colCount[] = new int[250];
        int[] guardPos = new int[2];
        boolean guardFound = false;
        char guardDir = '^';

        HashMap<Character, int[]> directions = new HashMap<>();
        directions.put('^', new int[]{-1, 0});
        directions.put('>', new int[]{0, 1});
        directions.put('v', new int[]{1, 0});
        directions.put('<', new int[]{0, -1});

        Character[] turnOrder = {'^', '>', 'v', '<'};

        Set<String> totalPossibilities = new HashSet<>();
        int initialXPos = 0;
        int initialYPos = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                input[lineCount] = line;
                for (int i = 0; i < line.length(); i++) {
                    if (!guardFound) {
                        for (char c : turnOrder) {
                            if (line.charAt(i) == c) {
                                guardPos[0] = lineCount;
                                guardPos[1] = i;
                                initialXPos = guardPos[0];
                                initialYPos = guardPos[1];
                                guardDir = line.charAt(i);
                                guardFound = true;
                                break;
                            }
                        }
                    }
                }
                colCount[lineCount] = line.length();
                lineCount++;
            }
        } catch (IOException e) {
            System.out.println("Could not open file");
            System.exit(lineCount);
        }

        // Iterate through all positions to place a potential obstruction
        for (int i = 0; i < lineCount; i++) {
            for (int j = 0; j < colCount[i]; j++) {
                if (input[i].charAt(j) != '#' && !(i == initialXPos && j == initialYPos)) {
                    char originalChar = input[i].charAt(j);
                    input[i] = input[i].substring(0, j) + '#' + input[i].substring(j + 1);
                    if (isInfiniteLoop(input, guardPos[0], guardPos[1], directions, guardDir, lineCount, turnOrder)) {
                        totalPossibilities.add(i + "," + j);
                    }
                    input[i] = input[i].substring(0, j) + originalChar + input[i].substring(j + 1);
                }
            }
        }

        System.out.println("Final answer? " + totalPossibilities.size());
    }

    public static boolean isWithinBounds(int[] pos, int rows, int cols) {
        return (pos[0] >= 0 && pos[0] < rows && pos[1] >= 0 && pos[1] < cols);
    }

    public static boolean isInfiniteLoop(String[] input, int startX, int startY, HashMap<Character, int[]> directions,
                                         char guardDir, int rows, Character[] turnOrder) {
        Set<String> visitedPath = new HashSet<>();
        int dirIndex = Arrays.asList(turnOrder).indexOf(guardDir);
        visitedPath.add(startX + "," + startY + ":" + dirIndex);

        int cols = input[startX].length();
        int iterations = 0;

        while (true) {
            iterations++;
            if (iterations > 10000) {
                // Safeguard against excessive iterations
                return false;
            }

            int[] dir = directions.get(guardDir);
            int[] newPos = {startX + dir[0], startY + dir[1]};

            if (isWithinBounds(newPos, rows, cols) && input[newPos[0]].charAt(newPos[1]) != '#') {
                startX = newPos[0];
                startY = newPos[1];
                if (visitedPath.contains(startX + "," + startY + ":" + dirIndex)) {
                    return true;
                }
                visitedPath.add(startX + "," + startY + ":" + dirIndex);
            } else {
                // Turn right if there's an obstacle
                dirIndex = (dirIndex + 1) % 4;
                guardDir = turnOrder[dirIndex];
            }
        }
    }
}
