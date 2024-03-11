public class arraytask_4
{
  public static void main(String[]args)
  {
    int[] a = new int[] {10, 30, 20, 50, 40};
    int max=a[0];
    int maxloc=a[0];
    for(int i=0;i<a.length;i++)
    {
      if(a[i]>max){
        max=a[i];
        maxloc=i;
      }
    }
    int x=a[0];
    a[0]=a[maxloc];
    a[maxloc]=x;
    for(int i=0; i<a.length;i++)
    {
      System.out.print("," + a[i]);
    }
  }
}
        