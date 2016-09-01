import java.io.*;
import java.util.Scanner;

public class Youngest
{
   private static final int FILE_IDX = 0;
   private static final int MIN_ARGS = 1;

   private static boolean verifyArguments(String [] args)
   {
      return args.length >= MIN_ARGS;
   }

   private static void findYoungest(Scanner in)
   {
      String name = "None";
      int age = 0;
      while (in.hasNextLine())
      {
         String [] words = in.nextLine().split("\\s");
         int new_age = Integer.parseInt(words[1]);
         if (age == 0 || new_age < age)
         {
            name = words[0];
            age = new_age;
         }
      }

      if (age == 0)
      {
         System.out.println("No persons");
      }
      else
      {
         System.out.println(name + " is the youngest, age " + age);
      }
   }

   public static void main(String [] args)
   {
      try
      {
         if (verifyArguments(args))
         {
            Scanner in = new Scanner(new FileInputStream(args[FILE_IDX]));
            findYoungest(in);
         }
         else
         {
            System.err.println("missing filename");
         }
      }
      catch (FileNotFoundException e)
      {
         System.err.println(e.getMessage());
      }
   }
}