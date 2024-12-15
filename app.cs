using System;
using System.Collections.Generic;

namespace CharLang
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Char programming language!");
            Console.WriteLine("Type 'exit' to quit.");

            while (true)
            {
                Console.Write("> ");
                string input = Console.ReadLine();

                if (input.ToLower() == "exit")
                    break;

                ExecuteCommand(input);
            }
        }

        static void ExecuteCommand(string command)
        {
            // Simple interpreter logic
            switch (command.ToLower())
            {
                case "hello":
                    Console.WriteLine("Hello, world!");
                    break;
                case "date":
                    Console.WriteLine(DateTime.Now);
                    break;
                default:
                    Console.WriteLine("Unknown command");
                    break;
            }
        }
    }
}

