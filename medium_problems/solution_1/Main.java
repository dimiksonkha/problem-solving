import java.util.Scanner;  // Import the Scanner class
import java.util.ArrayList; // import the ArrayList class
import java.util.*;
import java.lang.*;
import java.io.*;



public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);  // Create a Scanner object
    ArrayList<Student> students = new ArrayList<Student>(); // Create an ArrayList object
    
    int numberOfStudent = input.nextInt();  // Read user input
    for (int i = 0; i <numberOfStudent ; i++) {
     String studentInfo =input.nextLine;
     Student student = new Student();
     String[] splitedStudentInfo = studentInfo.split(" ");
     student.setID(splitedStudentInfo[0])
     student.setName(splitedStudentInfo[1])
     student.setCGPA(splitedStudentInfo[2])
     students.add(student);
     

}
 

  }
  
  Collections.sort(students, new SortByCGPA());
  
  Collections.sort(students, new SortByName());
  
  Collections.sort(students, new SortByID());
  
  for (int i=0; i<students.size(); i++)
            System.out.println(ar.get(i));
  
  

  class SortByCGPA implements Comparator<Student>
{
    
    public int compare(Student a, Student b)
    {
        return b.cgpa - a.cgpa;
    }
}

  class SortByName implements Comparator<Student>
{
    public int compare(Student a, Student b)
    {
        return a.name - b.name;
    }
}

  class SortByID implements Comparator<Student>
{
    
    public int compare(Student a, Student b)
    {
        return a.id - b.id;
    }
}

}

