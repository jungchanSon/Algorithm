public class 자바연습 {
    public static void main(String[] args) {
        String s1 = "1";
        String s2 = "1";
        System.out.println(s1 == "1");
        System.out.println(s1.equals("1"));
        User a = new User("gyoogle");   // 1
        System.out.println("a.name: " + a.name);
        System.out.println("a 객체의 주소 : " + System.identityHashCode(a));
        System.out.println("a 객체의 name 주소 : " + System.identityHashCode(a.name));
        System.out.println("---foo 함수 실행---");
        foo(a);
        System.out.println("a.name : " + a.name);
        System.out.println("a 객체의 주소 : " + System.identityHashCode(a));
        System.out.println("a 객체의 name 주소 : " + System.identityHashCode(a.name));
    }
    public static void foo(User b){        // 2
        b.name = "ASD";
        b = new User("jongnan");    // 3
    }
}

class User{
    public String name;

    User(String name){
        this.name = name;
    }
}

/* 
실행 결과

a.name: gyoogle
a 객체의 주소 : 1392838282
a 객체의 name 주소 : 523429237
---foo 함수 실행---
a.name : ASD
a 객체의 주소 : 1392838282
a 객체의 name 주소 : 664740647
*/