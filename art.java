import java.util.Scanner;

class art{
    public static void main(String[] args) {
        // System.out.println("hi 放松心情");
        String tmp;
        // Tana tana1 = new Tana("zzw");
        Tana tana2 = new Tana();
        Scanner inp = new Scanner(System.in);

        System.out.println("Enter Your frist gf Name:");
        tmp = inp.nextLine();
        tana2.setGrilName(tmp);
        // tana1.saying();
        tana2.saying();
        

    }
}