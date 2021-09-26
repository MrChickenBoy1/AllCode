using System;
using System.Threading;


namespace Calc
{
    class Input
    {
        static void Main()
        {
            
                    
            Console.WriteLine("---------- + for Addition | - for Subtraction | / for Division | X for Multiplication ----------");
            Console.WriteLine("---------- = for answer ----------");
            Console.WriteLine("________________________________________________________________________________________________");
            Console.WriteLine("");
            
            
            Console.WriteLine("What number do you choose?");
            string number_str = Console.ReadLine();

            Operation(ref number_str);
        }
        static void Operation(ref string number_str)
            
        {
            int total_number = 0;  

            string Answer = "NONE";

            string number_str_2 = "0";

            
            Console.WriteLine("What operation? ");
            string Operation = Console.ReadLine();

            while (Operation != "+" && Operation != "-" && Operation != "/" && Operation != "*" && Operation != "=")
            {
                Console.WriteLine("What operation? ");
                Operation = Console.ReadLine();
            }
            
            while (Answer != "=")
            {

                switch (Operation)
                {
                    case "+":
                    {
                        Addition(ref total_number, ref number_str, ref number_str_2);
                        break;
                    }
                    case "-":
                    {
                        Subtraction(ref total_number, ref number_str, ref number_str_2);
                        break;
                    }
                    case "/":
                    {
                        Division(ref total_number,ref number_str, ref number_str_2);
                        break;
                    }
                    case "*":
                    {
                        Multiplication(ref total_number,ref number_str, ref number_str_2);
                        break;
                    }
                    case "=":
                    {
                        Console.WriteLine(number_str);
                        Answer = "=";
                        Environment.Exit(0);
                        break;
                    }
                }

                if (Answer == "=")
                {
                    break;
                }

                else
                {
                    Console.WriteLine("What operation? ");
                    Operation = Console.ReadLine();

                    while (Operation != "+" && Operation != "-" && Operation != "/" && Operation != "*" && Operation != "=")
                    {
                        Console.WriteLine("What operation? ");
                        Operation = Console.ReadLine();
                        
                    }
                }
                

                
            }
        }

        static void Addition (ref int total_number,ref string number_str, ref string number_str_2)
            
        {   
            Console.WriteLine("What number do you choose?");
            number_str_2 = Console.ReadLine();

            int number_int = Convert.ToInt32(number_str);
            int number_int_2 = Convert.ToInt32(number_str_2);
            
            int added_number = number_int + number_int_2;

            total_number += added_number;

            string total_number_str = total_number.ToString();
            
            Operation(ref total_number_str);
                        
        }

        static void Subtraction (ref int total_number,ref string number_str, ref string number_str_2)
            
        {  
            Console.WriteLine("What number do you choose?");
            number_str_2 = Console.ReadLine();

            int number_int = Convert.ToInt32(number_str);
            int number_int_2 = Convert.ToInt32(number_str_2);
            
            int subtracted_number = number_int_2 - number_int;

            total_number -= subtracted_number;
            string total_number_str = total_number.ToString();
            
            Operation(ref total_number_str);
        }

        static void Multiplication (ref int total_number,ref string number_str, ref string number_str_2)
            
        {   

            Console.WriteLine("What number do you choose?");
            number_str_2 = Console.ReadLine();

            int number_int = Convert.ToInt32(number_str);
            int number_int_2 = Convert.ToInt32(number_str_2);
            

            total_number = number_int * number_int_2;
            string total_number_str = total_number.ToString();
            
            Operation(ref total_number_str);
        }

        static void Division (ref int total_number,ref string number_str, ref string number_str_2)
            
        {                         

            Console.WriteLine("What number do you choose?");
            number_str_2 = Console.ReadLine();

            int number_int = Convert.ToInt32(number_str);
            int number_int_2 = Convert.ToInt32(number_str_2);
            
            total_number = number_int / number_int_2;
            string total_number_str = total_number.ToString();
            
            Operation(ref total_number_str);        
        }


    }

}