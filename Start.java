import java.util.Scanner;

class Persona {
    String nome;
    int eta;

    public Persona(String nome, int eta) {
        this.nome = nome;
        this.eta = eta;
    }

    public void saluta() {
        System.out.println("Ciao io sono " + this.nome + " e ho " + this.eta + " anni");
    }
}   

public class Start {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Inserire il nome: ");
        String nome = scanner.nextLine();

        System.out.println("Inserire l'età: ");
        int eta = scanner.nextInt();
        scanner.nextLine();

        Persona persona = new Persona(nome, eta);
        persona.saluta();
    }
}