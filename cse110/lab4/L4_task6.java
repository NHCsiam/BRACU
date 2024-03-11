import java.util.Scanner;
public class L4_task6
{
  public static void main(String[]args)
  {
    System.out.println("Enter the quantity:");
    Scanner keyboard=new Scanner (System.in);
    int number=keyboard.nextInt();
    int i;
    for(i=1; i<=number ; i++){
      int num=keyboard.nextInt();
      if(num%2==0){
        System.out.println("even");
      }
      else {
        System.out.println("odd");
      }
    }
  }
}
    