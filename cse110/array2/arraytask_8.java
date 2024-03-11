import java.util.Scanner;
public class arraytask_8
{
  public static void main(String[]args)
  {
    System.out.println("enter the number");
    Scanner keyboard=new Scanner(System.in);
    int n=keyboard.nextInt();
    int[]a=new int[n];
    for(int x=0;x<a.length;x++)
    {
      System.out.println("index num:");
      a[x]=keyboard.nextInt();
      int max;
      int temp=0;
      for(int i=0;i<a.length;i++)
      {
         max=i;
        for(int j=i+1;j<a.length;j++)
        {
          if(a[j]>a[max])
          {
            max=j;
          }
        }
        temp=a[i];
        a[i]=a[max];
        a[max]=temp;
        System.out.print(a[i] + ",");
      }
    }
    if(a.length%2!=0){
      System.out.println("the median is" + a[a.length/2]);
    }
    else{
      System.out.println("the median is" + (a[a.length/2]+a[a.length/2-1])/2);
    }
  }
}

    