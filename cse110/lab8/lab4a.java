import java.util.Scanner;
public class lab4a{
  public static void main (Strings[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter a number");
    int num=sc.nextInt();
    int divcount=0;
    for(int i=1;i<=num;i++);
    {
      if (num%i==0){
        divcount++;
      }
    }
    if(divcount==2)
    {
      system.out.println("not prime");
    }
    else{
      System.out.print("prime");
    }
  }
}
   
    