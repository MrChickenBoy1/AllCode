using System;
using System.Threading;


namespace Tables
{
    class Program
    {
        int smallestRange;
        int largestRange;


     
        static void Main()
            
        {
            Random random = new Random();

            Console.WriteLine("What is the smallest number for the range? ");
            string smallestRangeStr = Console.ReadLine();
            int smallestRange = Convert.ToInt32(smallestRangeStr);

            Console.WriteLine("What is the largest number for the range? ");
            string largestRangeStr = Console.ReadLine();
            int largestRange = Convert.ToInt32(largestRangeStr);

            int number = random.Next(smallestRange, largestRange + 1);
            
            Console.WriteLine("Choosing number");
            Thread.Sleep(500);
            Console.WriteLine(".");
            Thread.Sleep(500);
            Console.WriteLine(".");
            Thread.Sleep(500);
            Console.WriteLine(".");
            
            Console.WriteLine("Number choosen!");
            Thread.Sleep(500);
            
            Console.WriteLine($"What number between {smallestRange} and {largestRange} do you guess?" );
            string guess = Console.ReadLine();
            
            int guessInt = Convert.ToInt32(guess);
            
            while (guessInt != number)
            {
                if (guessInt < number)
                {
                    
                    if (guessInt < number && guessInt > number - 5)
                    {
                        Console.WriteLine("Not right, you're close but your number is less than the number chosen");
                    }
                    
                    else
                    {
                                
                        Console.WriteLine("Not right. Your number is smaller than the number chosen");
                    }

                }
                else if (guessInt > number)
                {
                    
                    if (guessInt > number && guessInt < number + 5)
                    {
                        Console.WriteLine("Not right, you're close but your number is more than the number chosen");
                    }
                    
                    else 
                    {
                        Console.WriteLine("Not right. Your number is bigger than the number chosen");
                    }

                }

                
                    
                Console.WriteLine($"What number between {smallestRange} and {largestRange} do you guess?");
                guess = Console.ReadLine();
            
                guessInt = Convert.ToInt32(guess);
                

            }
        }
    }
}