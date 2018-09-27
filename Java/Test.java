import java.util.Scanner;

public class Test
{
	public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = reader.nextInt(); 
        reader.close();
        System.out.println("2 vs you number: "+n*2);
	}
}