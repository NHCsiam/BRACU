public class arraytask_2
{
  public static void main(String[]args)
  {
    int[] marks = new int[] {10, 30, 20, 50, 40};
    int sum=0;
    int avg;
    int count=0;
    for(int i=0;i<marks.length;i++)
    {
      sum=sum+marks[i];
    }
    avg=sum/marks.length;
    for(int i=0; i<marks.length;i++)
    {
      if (marks[i]>avg){
        count++;}
    }
    System.out.println(count +"Better than average");
    for(int s=0;s<marks.length;s++)
    {
      if(marks[s]>avg){
        System.out.println("They received following marks" + marks[s]);
      }
    }
  }
}
      