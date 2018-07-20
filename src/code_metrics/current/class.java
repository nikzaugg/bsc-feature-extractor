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

    public void setx(String foo){
        this.foo = foo;
        // this is a comment
    }

    public void sety(String foo){
        this.foo = foo;
    }

    public void x(String foo){
        this.foo = foo;
    }

    public void df(String foo){
        this.foo = foo;
    }

    public void h(String foo){
        this.foo = foo;
    }

    public void e(String foo){
        this.foo = foo;
    }

    public void u(String foo){
        this.foo = foo;
    }
}