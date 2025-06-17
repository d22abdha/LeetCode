using System;
using System.Collections.Generic;




namespace Room_painting
{
     class Program
    {
        static void Main()
        {
            var firstLine = Console.ReadLine().Split();
            int numberOfcans = int.Parse(firstLine[0]);
            int numberOfneeds = int.Parse(firstLine[1]);


            List<int> canList = new List<int>();

            for (int i = 0; i < numberOfcans; i++) 
            {
                //user writes in the numberOfcans one by one until the max
                int cans = int.Parse(Console.ReadLine());
                // add to the list everytime the user writes in: so we add cans to the canList
                canList.Add(cans);

            }

            // we sort the canList so we can find the smallest faster
            canList.Sort();

            List<int> canNeedsList = new List<int>();

            for (int i =0; i < numberOfneeds; i++)
            {

                int canNeeds = int.Parse(Console.ReadLine());
                canNeedsList.Add(canNeeds);
            }

            // we need to calculate the amount of cans wasted 
            int TotalWaste = 0;

            foreach (int canNeeds in canNeedsList)
            { 
            
                foreach (int cans in canList)
                    {
                    if (cans >= canNeeds)
                    {
                        TotalWaste += (cans - canNeeds);
                        break;
                    }
                }
            }


            Console.WriteLine(TotalWaste);
            Console.ReadKey();
        }

    }

}
