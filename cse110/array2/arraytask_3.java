public class arraytask_3 
{
  public static void main(String[]args)
  {
    int[] a = new int[] {10, 30, 20, 50, 40};
    int max=a[0];
    int maxloc=0;
    for(int i=1; i<a.length;i++)
    {
      if(max<a[i]){
        max=a[i];
        maxloc= i;
      }
    }
    System.out.println("Largest mark is" + max);
    System.out.println(maxloc);
  }
}