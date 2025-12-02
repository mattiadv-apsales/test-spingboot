import java.util.Scanner;
import java.util.ArrayList;

class Rub {
    String nome;
    String numero;

    public Rub(String nome, String numero) {
        this.nome = nome;
        this.numero = numero;
    }

    public void mostraContatto() {
        System.out.println("Contatto: " + this.nome + ", Numero: " + this.numero);
    }
};

public class Rubrica {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Rub> contatti = new ArrayList<>();
        while (true) {
            System.out.println("1) Aggiungi contatto\n2) Mostra contatti\n3) Esci\n");
            int scelta = scanner.nextInt();
            scanner.nextLine();

            if (scelta == 1) {
                System.out.println("Inserire nome contatto: ");
                String nome = scanner.nextLine();

                System.out.println("Inserire il numero del contatto: ");
                String numero = scanner.nextLine();

                Rub contatto = new Rub(nome, numero);
                contatti.add(contatto);
            } else if (scelta == 2) {
                for (Rub rub : contatti) {
                    rub.mostraContatto();
                }
            } else if (scelta == 3) {
                System.out.println("Ciao ciaoooo!");
                break;
            } else {
                System.out.println("Inserire una scelta valida.");
            }
        }
    }
}
