import java.util.Scanner;
public class arraytask_10
{
  public static void main(String[]args)
  {
    Scanner sc=new Scanner(System.in);
    int quantity=sc.nextInt();
    int num[]=new int[quantity];
    for(int i=0;i<quantity;i++)
    {
      num[i]=sc.nextInt();
      int c=0;
      for(int j=0;j<i;j++)
      {
        if(!(num[i]>num[j])){
          c=1;
        }
      }
      if(c==0){ 
        System.out.println("Yes");
      }
      else{ 
        System.out.println("No");
      }
    }
  }
}