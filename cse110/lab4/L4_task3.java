public class L4_task3
{
  public static void main(String[]args)
  {
     int count; int sum=0;
     for(count=1; count<=600 ; count++)
       if(count%7==0)
     {
     sum=sum+count;
     }
     else if(count%9==0)
     {
       sum=sum+count;
     }
     System.out.println(sum);
  }
}