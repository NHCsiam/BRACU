public class arraytask_5
{
  public static void main(String[]args)
  {
    int[] a = new int[] {50, 30, 20, 10, 40};
    int max =a[1];
    int maxloc= a[1];
    for(int i=2;i<a.length;i++)
    {
      if(a[i]>max){
        max=a[i];
        maxloc=i;
      }
    }
    int x=a[1];
    a[1]=a[maxloc];
    a[maxloc]=x;
    for(int i=0;i<a.length;i++)
    {
      System.out.print(a[i] + ",");
    }
  }
}
    