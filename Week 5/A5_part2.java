import java.io.*;
import java.util.*;


class A5_part2{

        public static void main(String args[])throws Exception{

                File file = new File("people.txt");
                Scanner scan = new Scanner(file);
                int lineNumber = 1;
                while (scan.hasNextLine()){
                        String line = scan.nextLine();
                        if (line.contains("gmail.com")){
                            System.out.println(line + " matched");
                        }
                        lineNumber++;

                    }
                scan.close();

            

        }//end of main


}//end of class