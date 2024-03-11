public class arraytask_7
{
  public static void main(String[]args)
  {
    int[] a = new int[] {50, 30, 20, 10, 40};
    int max;
    int temp=0;
    for (int i=0;i<a.length;i++)
    {
      max=i;
      for(int j=i+1;j<a.length;j++)
      {
        if(a[j]>a[max]){
          max=j;
        }
      }
      temp=a[i];
      a[i]=a[max];
      a[max]=temp;
    }
    for(int i=0;i<a.length;i++)
    {
      System.out.print(a[i] + ",");
    }
  }
}
