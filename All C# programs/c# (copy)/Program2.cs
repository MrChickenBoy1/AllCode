using System;

namespace Tables
{
    class Program
    {
        static void Main()
            
        {
            Console.WriteLine("What number of table do you want?");
            int number = Convert.ToInt32(Console.ReadLine());
            int tablenum = 0;


            Console.WriteLine("---------------------------------");
            
            Console.WriteLine("What is the length of the table?");

            Console.WriteLine("---------------------------------");


            int length = Convert.ToInt32(Console.ReadLine());

            for (int i = 0; i < length; i ++)
            {
                Console.WriteLine(tablenum + number);
                tablenum += 2;
            }
        }
    }
}
