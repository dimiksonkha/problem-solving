public class Student{
    int id;
    String name;
    double cgpa;
    
    public Student(int id, String name, double cgpa){
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }
    
    public void setID(int id){
        this.id=id;
        
    }
    
    public void setName(String name){
        this.name=name;
        
    }
    
    public void setCGPA(int cgpa){
        this.cgpa=cgpa;
        
    }
    
    public int getID(){
        return this.id;
        
    }
    
    public String getName(){
        return this.name;
        
    }
    
    public int getCGPA(){
        return this.cgpa;
        
    }
    
    public String toString()
    {
        return this.id + " " + this.name +
                           " " + this.cgpa;
    }
    
}
