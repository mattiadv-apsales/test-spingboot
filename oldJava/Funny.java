package oldJava;
import java.util.Scanner;
import java.util.ArrayList;

class Person {
    public String name;
    public String surname;
    public int eta;

    public Person(String name, String surname, int eta) {
        this.name = name;
        this.surname = surname;
        this.eta = eta;
    }

    public void presentation() {
        System.out.println("Hi i'm " + this.name + " " + this.surname + " and i'm " + this.eta + " years old");
    }

    public boolean isAdult() {
        if (this.eta >= 18) {
            return true;
        } else {
            return false;
        }
    }
}

public class Funny {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String cont = "";
        ArrayList<Person> persons = new ArrayList<>();
        while (true) {
            System.out.println("1) Add\n2) View all\n3) Research by name\n4) Exit\nChoose:");
            cont = scanner.nextLine();

            switch (cont) {
                case "1":
                    System.out.println("Name: ");
                    String name = scanner.nextLine();
                    System.out.println("Surname: ");
                    String surname = scanner.nextLine();
                    System.out.println("Age: ");
                    int age = scanner.nextInt();
                    scanner.nextLine();

                    Person new_person = new Person(name, surname, age);
                    persons.add(new_person);
                    break;
                
                case "2":
                    persons.sort((p1, p2) -> Integer.compare(p1.eta, p2.eta));
                    for (Person per : persons) {
                        per.presentation();
                        if (per.isAdult() == true) {
                            System.out.println("It's an adult\n");
                        } else {
                            System.out.println("It's not an adult\n");
                        }
                    }
                    System.out.println("\n\n");
                    break;

                case "3":
                    System.out.println("Reasearch by the name: ");
                    String research_name = scanner.nextLine();
                    boolean founded = false;

                    for (Person per : persons) {
                        if (per.name.equalsIgnoreCase(research_name)) {
                            per.presentation();
                            System.out.println("The guy " + per.name + " found!\n\n");
                            founded = true;
                        }
                    }

                    if (founded == false) {
                        System.out.println("The guy " + research_name + " doesn't exist!\n\n");
                    }
                    break;

                case "4":
                    return;

                default:
                    System.out.println("Insert a valid choice\n\n");
            }
        }

    }
}