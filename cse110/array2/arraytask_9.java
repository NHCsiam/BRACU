import java.util.Scanner;
public class arraytask_9
{
  public static void main(String[]args)
  {
  Scanner sc=new Scanner(System.in);
  int quantity=sc.nextInt();
  int id[]=new int[quantity];
  String full_name[]=new String[quantity];
  double mark[]=new double[quantity];
  double sum=0;
  double average=0.0;
    for(int i=0;i<quantity;i++)
    {
     System.out.print("Give ID :");
      id[i]=sc.nextInt();
     System.out.print("Give Name :");
      full_name[i]=sc.next();
     System.out.print("Give Mark :");
      mark[i]=sc.nextDouble();
      sum=sum+mark[i];
    }
    average=sum/quantity;
    System.out.println("Average mark : "+average);
    for(int j=0;j<quantity;j++){
      System.out.println(full_name[j]+" : "+id[j]);
    }
  }
}