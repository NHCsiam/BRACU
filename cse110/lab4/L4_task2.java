public class L4_task2
{
  public static void main(String[]args)
  {
    int count=1;
    int sum =0;
    while (count<=600){
      if (count%7==0){
        if (count%9==0){
          sum=sum+count;
        }
      }
      count++;
    }
    System.out.println(sum);
  }
}