import java.io.*;
import java.util.*;

public class sol_2 {
    public static void main(String[] args) {
        String input[] = new String[250];
        int lineCount = 0;
        int colCount[] = new int[250];
        int guardPos[] = new int[5];
        boolean guardFound = false;
        char guardDir = '^';

        HashMap<Character, int[]> directions = new HashMap<>();
        directions.put('^',new int[]{-1,0});
        directions.put('>', new int[]{0,1});
        directions.put('v', new int[]{1,0});
        directions.put('<', new int[]{0,-1});

        Character[] turnOrder = {'^','>','v','<'};

        Set<String> totalPosibilities = new HashSet<>();
        int initialXPos = 0;
        int initialYPos = 0;

        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            String line;
            while ((line = reader.readLine()) != null) {
                input[lineCount] = line;
                for (int i = 0; i < line.length(); i++) {
                    if(!guardFound)
                    {   
                        for(char c : turnOrder)
                        {
                            if(line.charAt(i) == c)
                            {
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
                // input += line + "\n";
                // System.out.println(input[lineCount-1]);
                // System.out.println();
            }
        } catch (IOException e) {
            System.out.println("Could not open file");
            System.exit(lineCount);
         
        }
        // System.out.println("Guard pos: "+ guardPos[0] +" , " + guardPos[1]);
        // for(int[] obstacle : obstacles)
        // {
        //     System.out.println("Obstacle: " + obstacle[0] + " , " + obstacle[1]);
        // }
        for(int i = 0; i < lineCount; i++){
            for (int j = 0; j < colCount[i]; j++) {
                if(input[i].charAt(j) != '#' && i!=initialXPos && j!=initialYPos)
                {
                    char ogChar = input[i].charAt(j);
                    input[i] = input[i].substring(0, j) + '#' + input[i].substring(j + 1);
                    int dirIndex = Arrays.asList(turnOrder).indexOf(guardDir);
                    if(isInfiniteLoop(input, guardPos[0], guardPos[1], directions, guardDir, lineCount, turnOrder))
                    {
                        totalPosibilities.add(i + "," + j);
                    }
                    input[i] = input[i].substring(0, j) + ogChar + input[i].substring(j+1);
                }
            }
        }
        System.out.println("Final answer? " + totalPosibilities.size());

    }
    public static boolean isWithinBounds(int[] pos, int rows, int cols)
    {
        return (pos[0]<rows && pos[1]<cols && pos[0]>=0 && pos[1]>=0);
    }

    public static boolean isInfiniteLoop(String[] input, int startX, int startY,  HashMap<Character, int[]> directions, char guardDir, int rows, Character[] turnOrder)
    {
        Set<String> visitedPath = new HashSet<>();
        int dirIndex = Arrays.asList(turnOrder).indexOf(guardDir);
        visitedPath.add(startX + "," + startY  + ":" + dirIndex);
        int iterations = 0;
        while (true) { 
            iterations++;
            int dir[] = directions.get(guardDir);
            int newPos[] = {startX + dir[0] , startY + dir[1]};
            if(iterations > 50)
            {
                break;
            }
            if(isWithinBounds(newPos, rows, input[startX].length()))
            {
                if(input[newPos[0]].charAt(newPos[1]) != '#')
                {
                    startX = newPos[0];
                    startY = newPos[1];
                    if(visitedPath.contains(startX + "," + startY  + ":" + dirIndex))
                    {
                        System.out.println("infinite path found");
                        return true;
                    }
                    visitedPath.add(startX + "," + startY  + ":" + dirIndex);
                    // death machine: System.out.println("changing startX and startY: " + startX + " , " + startY);
                }
                else
                {
                    guardDir = turnOrder[(dirIndex + 1) % 4];
                    dirIndex = Arrays.asList(turnOrder).indexOf(guardDir);
                    
                    System.out.println("changing direction: " + guardDir + " at " + newPos[0] + " , " + newPos[1]);
                }
            }
            
            else
            {
                break;
            }
        }
        return false;
    }

}

// @SuppressWarnings("RedundantStringConstructorCall")
// public static void main(String[] args) {

//     String input[] = new String[250];
//     int lineCount = 0;
//     int colCount[] = new int[250];
//     int guardPos[] = new int[5];
//     boolean guardFound = false;
//     char guardDir = '^';
//     HashMap<Character, int[]> directions = new HashMap<>();
//     directions.put('^',new int[]{-1,0});
//     directions.put('>', new int[]{0,1});
//     directions.put('v', new int[]{1,0});
//     directions.put('<', new int[]{0,-1});

//     Character[] turnOrder = {'^','>','v','<'};
//     //create hashSet for all seen tiles
//     Set<String> path = new HashSet<>();
//     //Set<String> obstacles = new HashSet<>();
    
    
//     try {
//         BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
//         String line;
//         while ((line = reader.readLine()) != null) {
//             input[lineCount] = line;
//             for (int i = 0; i < line.length(); i++) {
//                 if(!guardFound)
//                 {   
//                     for(char c : turnOrder)
//                     {
//                         if(line.charAt(i) == c)
//                         {
//                             guardPos[0] = lineCount;
//                             guardPos[1] = i;
//                             guardDir = line.charAt(i);
//                             guardFound = true;
//                             break;
//                         }
//                     }
                    
//                 }
//             }
//             colCount[lineCount] = line.length();
//             lineCount++;
//             // input += line + "\n";
//             // System.out.println(input[lineCount-1]);
//             // System.out.println();
//         }
//     } catch (IOException e) {
//         System.out.println("Could not open file");
//         System.exit(lineCount);
        
//     }
//     // System.out.println("Guard pos: "+ guardPos[0] +" , " + guardPos[1]);
//     // for(int[] obstacle : obstacles)
//     // {
//     //     System.out.println("Obstacle: " + obstacle[0] + " , " + obstacle[1]);
//     // }
//     int totalPosibilites = 0;
//     //obstacles.add(guardPos[0]+","+guardPos[1]);

//     for(int i = 0; i < lineCount; i++){
//         for (int j = 0; j < colCount[i]; j++) {
//             if(input[i].charAt(j) == '.')
//             {
//                 String[] input_copy = new String[input.length];

//                 for (int k = 0; k < input.length; k++) {
//                     if(input[k] != null)
//                     {
//                         input_copy[k] = new String(input[k]);
//                         input_copy[i] = input_copy[i].substring(0, j) + '#' + input_copy[i].substring(j + 1);
//                         System.out.println(input_copy[k]);
//                         break;
//                     }
                        
//                 }
//                 input_copy[i] = input_copy[i].substring(0, j) + '#' + input_copy[i].substring(j + 1);

//                 while (isWithinBounds(guardPos, lineCount, input[guardPos[0]].length())) { 
//                     path.add(guardPos[0]+","+guardPos[1]+":"+guardDir);
//                     int dir[] = directions.get(guardDir);
//                     //System.out.println("changes to do: "+ dir[0]+ " , " + dir[1]);
//                     int newPos[] = {guardPos[0] + dir[0] , guardPos[1] + dir[1]};
//                     if(isWithinBounds(newPos, lineCount, input[guardPos[0]].length()))
//                     {
//                         System.out.println("Directions changed, newPos:" + (newPos[0]+1) + " , " + (newPos[1]+1));
//                         if((input_copy[newPos[0]].charAt(newPos[1]) == '#'))
//                         {
//                             int currentDirIndex = Arrays.asList(turnOrder).indexOf(guardDir);
//                             guardDir = turnOrder[(currentDirIndex + 1) % 4];
//                             dir = directions.get(guardDir);
//                             newPos = new int[]{guardPos[0] + dir[0] , guardPos[1] + dir[1]};
//                             if(path.contains(newPos[0]+","+newPos[1]+":"+guardDir))
//                             {
//                                 totalPosibilites++;
//                             }
//                             guardPos[0] = newPos[0];
//                             guardPos[1] = newPos[1];
//                             if(isWithinBounds(guardPos, lineCount, input[guardPos[0]].length()))
//                             {
//                                 path.add(newPos[0] + "," + newPos[1]);
//                             }
                            
//                             //System.out.println("Directions changed, newPos:" + (newPos[0]+1) + " , " + (newPos[1]+1));
//                         }  
//                         else if(input_copy[newPos[0]].charAt(newPos[1]) != '#')
//                         {
//                             guardPos[0] = newPos[0];
//                             guardPos[1] = newPos[1];
//                             //System.out.println("new direction: "+ guardDir);
//                             if(isWithinBounds(guardPos, lineCount, input[guardPos[0]].length()))
//                             {
//                                 path.add(newPos[0] + "," + newPos[1]+":"+guardDir);
//                             }
//                             //System.out.println("newPos:" + newPos[0] + " , " + newPos[1]);
//                         }
                        
//                     }
//                     else
//                     {
//                         break;
//                     } 
//                 }
//             }
            
//         }
//     }
//     System.out.println("Total Possibilites: "+ totalPosibilites);
// }