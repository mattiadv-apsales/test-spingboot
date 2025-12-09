import java.util.Scanner;

class Citta {
    public int width;
    public int height;
    private int min = 0;
    private int max = 0;
    private int o_spawn = 0;
    private int street_spawn = 0;
    private int player_spawn_x = 0;
    private int player_spawn_y = 0;

    public Citta(int width, int height) {
        this.width = width;
        this.height = height;
        this.max = this.width - 1;
        this.min = 0;
        this.o_spawn = (int)(Math.random() * (this.max - this.min + 1)) + this.min;
        this.street_spawn = (int)(Math.random() * (this.max - this.min + 1) + this.min);
        this.player_spawn_x = this.width / 2;
        this.player_spawn_y = this.height / 2;
    }

    public void move(char dire) {
        switch (dire) {
            case 'w': if (this.player_spawn_y > 0) this.player_spawn_y -= 1; break;
            case 's': if (this.height - 1 > this.player_spawn_y) this.player_spawn_y += 1; break;
            case 'a': if (this.player_spawn_x > 0) this.player_spawn_x -= 1; break;
            case 'd': if (this.width - 1 > this.player_spawn_x) this.player_spawn_x += 1; break;
        }
    }

    public void viewCity() {
        for (int a = 0; a < this.height; a++) {
            this.o_spawn = (int)(Math.random() * (this.max - this.min + 1)) + this.min;
            this.street_spawn = (int)(Math.random() * (this.max - this.min + 1)) + this.min;

            while (this.o_spawn == this.street_spawn) {
                this.o_spawn = (int)(Math.random() * (this.max - this.min + 1)) + this.min;
                this.street_spawn = (int)(Math.random() * (this.max - this.min + 1)) + this.min;
            }

            for (int b = 0; b < this.width; b++) {
                if (a == this.player_spawn_y && b == this.player_spawn_x) {
                    System.out.print("@");
                } else if (b == this.o_spawn) {
                    System.out.print("O");
                } else if (b == this.street_spawn) {
                    System.out.print("-");
                } else {
                    System.out.print("+");
                }
            }
            System.out.println();
        }
    }
}

public class City {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Inserire la largheza della città: ");
        int width = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Inserire l'altezza della città: ");
        int height = scanner.nextInt();
        scanner.nextLine();

        System.out.println("\n\n");
        
        Citta crazy = new Citta(width, height);
        
        while (true) {
            System.out.println("\n\n");
            crazy.viewCity();

            System.out.print("Scegli se W, A, S, D e poi premi ENTER: ");
            String input = scanner.nextLine();

            if (input.equals("q")) {
                break;
            } else if (input.equals("")) {
                continue;
            } else {
                crazy.move(input.charAt(0));
            }
        }
    }
}