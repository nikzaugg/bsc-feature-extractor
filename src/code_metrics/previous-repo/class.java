public class Test {

    String foo;
    String bar;

    public static void main(String[] args) {
        Test test = new Test();
        test.setFoo("x");
    }

    public void setFoo(String foo){
        this.foo = foo;
        // this is a comment
        if (2 < 3) {
            System.out.println("higher");
        } else {
            System.out.println("lower");
        }
    }
}