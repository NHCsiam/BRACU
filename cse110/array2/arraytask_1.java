public class arraytask_1
{
  public static void main(String[]args)
  {
    int []marks=new int []{10,30,20,50,40};
    int sum=0;
    int max=marks[0];
    int min=marks[0];
    for(int i=0; i<marks.length;i++)
    {
      sum=sum+marks[i];
      if(max<marks[i]){
        max=marks[i];
      }
      if(min>marks[i])
      {
        min=marks[i];
      }
    }
    double avg;
    avg = sum/marks.length;
    System.out.println("Highest mark is" + max);
    System.out.println("Lowest  mark is" + min);
    System.out.println("Average mark is" + avg);
  }
}