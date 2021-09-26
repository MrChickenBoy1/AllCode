using System;

namespace Program
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Hello, welcome to the shop!");
            Console.WriteLine("What would you like to buy?");
            Console.WriteLine("Apple, Banana, Cake");
            string item = Console.ReadLine();
            
            item = item.ToLower();

            Console.WriteLine($"{item} Is that correct? (Y / N)");

            string Answer = Console.ReadLine();
            
            Answer = Answer.ToLower();

            if (Answer == "y")
            {
                if (item != "apple" && item != "banana" && item != "cake")
                {
                    Console.WriteLine("That's not in our shop!");
                }

                else if (item == "apple" || item == "banana" || item == "cake")
                {
                    Console.WriteLine("Cool");
                    Console.WriteLine("That will be $3.00. Please pay up");
                    string Money =  Console.ReadLine();
                    float MoneyInt = float.Parse(Money);
                    if (MoneyInt == 3)
                    {
                        Console.WriteLine("Awesome! Thanks a lot!");
                    }
                    else if (MoneyInt > 3) 
                    {
                        float change = MoneyInt - 3;
                        Console.WriteLine($"Oops! That is too much, change: ${change}");
                    }

                    else if (MoneyInt < 3)
                    {
                        Console.WriteLine($"Oh, you payed less, you can have the {item} for free!");
                    }


                }

            }

            
            if (Answer == "n")
            {
                Console.WriteLine("Run the program again.");

            }
        }
    }
}
