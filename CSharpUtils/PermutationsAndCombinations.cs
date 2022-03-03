using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine(PermutationNoRep(10, 10).ToString());
		Console.WriteLine(PermutationWithRep(10, 4).ToString());
		Console.WriteLine(CombinationWithRep(4, 4).ToString());
		Console.WriteLine(CombinationNoRep(4, 4).ToString());
	}
	
	public static int factorial(int x) {
		if(x == 0) {
			return 1;
		} else {
			int result = 1;
		while (x != 1) {
			result *= x;
			x -= 1;
		}
			return result;
		}
		
	}

	public static int PermutationWithRep(int numOfItems, int numOfChoices) {
		return (int)Math.Pow(numOfItems, numOfChoices);
	}
	
	public static int PermutationNoRep(int numOfItems, int numOfChoices) {
		return factorial(numOfItems) / factorial(numOfItems - numOfChoices);
	}
	
	public static int CombinationWithRep(int numOfItems, int numOfChoices) {
		return factorial(numOfItems + numOfChoices - 1) / (factorial(numOfChoices) * factorial(numOfItems - 1)); 
	}
	
	public static int CombinationNoRep(int numOfItems, int numOfChoices) {
		return factorial(numOfItems) / (factorial(numOfChoices) * factorial(numOfItems - numOfChoices)); 
	}
	
	
}
