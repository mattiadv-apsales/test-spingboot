import java.util.Scanner;
import java.io.File;

public class Shell {
    private static File currentDirectory = new File(System.getProperty("user.dir"));
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String before = "PinoOS";

        while (true) {
            System.out.print(currentDirectory.getAbsolutePath() + " > ");
            String input = scanner.nextLine();
            String[] parts = input.trim().split("\\s+");
            String command = parts[0];
            
            switch (command) {
                case "exit":
                    System.out.println(before + " > Exiting shell. Goodbye!");
                    return;
                case "hello":
                    System.out.println(before + " > Hello, User!");
                    break;
                case "ls":
                    File[] files = currentDirectory.listFiles();
                    if (files != null) {
                        for (File file : files) {
                            System.out.println(file.getName());
                        }
                    }
                    break;
                case "cd":
                    if (parts.length < 2) {
                        System.out.println(before + " > Error: 'cd' requires a directory name");
                        break;
                    }

                    // Ricostruisci l'intero path dopo "cd"
                    String rawPath = input.substring(3).trim(); // prende TUTTO dopo "cd "

                    // Rimuovi eventuali virgolette
                    if ((rawPath.startsWith("\"") && rawPath.endsWith("\"")) ||
                        (rawPath.startsWith("'") && rawPath.endsWith("'"))) {
                        rawPath = rawPath.substring(1, rawPath.length() - 1);
                    }

                    // Gestione speciale ".."
                    if (rawPath.equals("..")) {
                        File parent = currentDirectory.getParentFile();
                        if (parent != null) {
                            currentDirectory = parent;
                        } else {
                            System.out.println(before + " > Error: No parent directory");
                        }
                        break;
                    }

                    // Gestione percorso relativo
                    File dd = new File(currentDirectory, rawPath);

                    if (dd.exists() && dd.isDirectory()) {
                        currentDirectory = dd;
                    } else {
                        System.out.println(before + " > Error: Directory not found");
                    }
                    break;
                case "mkdir":
                    if (parts.length < 2) {
                        System.out.println(before + " > Error: The command 'mkdir' wait for a dirname");
                    } else {
                        String dirname = parts[1];
                        File newDir = new File(currentDirectory, dirname);
                        if (newDir.mkdir()) {
                            System.out.println(before + " > Directory '" + dirname + "' created");
                            break;
                        } else {
                            System.out.println(before + " > Error: Could not create directory");
                            break;
                        }
                    }
                    break;
                case "deldir":
                    if (parts.length < 2) {
                        System.out.println(before + " > Error: The command 'deldir' wait for a dirname");
                    } else {
                        String dirname = parts[1];
                        File dirToDelete = new File(currentDirectory, dirname);
                        if (dirToDelete.exists() && dirToDelete.isDirectory()) {
                            if (dirToDelete.delete()) {
                                System.out.println(before + " > Directory '" + dirname + "' deleted");
                                break;
                            } else {
                                System.out.println(before + " > Error: Could not delete directory (make sure it's empty)");
                                break;
                            }
                        } else {
                            System.out.println(before + " > Error: Directory not found");
                            break;
                        }
                    }
                    break;
                case "pwd":
                    System.out.println(currentDirectory.getAbsolutePath());
                    break;
                case "create":
                    if (parts.length < 2) {
                        System.out.println(before + " > Error: The command 'create' wait for a filename");
                    } else {
                        String filename = parts[1];
                        File newFile = new File(currentDirectory, filename);
                        try {
                            if (newFile.createNewFile()) {
                                System.out.println(before + " > File " + filename + " created");
                                break;
                            } else {
                                System.out.println(before + " > Error: File already exists");
                            }
                        } catch (Exception e) {
                            System.out.println(before + " > Error: Could not create file");
                            break;
                        }
                    }
                    break;
                case "delfile":
                    if (parts.length < 2) {
                        System.out.println(before + " > The command 'delfile' need a filename.");
                    } else {
                        String filename = parts[1];
                        File filetodelete = new File(currentDirectory, filename);
                        if (filetodelete.exists() && filetodelete.isFile()) {
                            if (filetodelete.delete()) {
                                System.out.println(before + " > File " + filename + " deleted");
                                break;
                            } else {
                                System.out.println(before + " > Error: Could not delete file");
                                break;
                            }
                        } else {
                            System.out.println(before + " > Error: File not found");
                            break;
                        }
                    }
                    break;
                case "cls":
                    for (int i = 0; i < 50; ++i) System.out.println();
                    break;
                case "help":
                    System.out.println("Available commands:");
                    System.out.println("hello - Greet the user");
                    System.out.println("ls - List files and directories");
                    System.out.println("cd <dirname> - Change directory");
                    System.out.println("mkdir <dirname> - Create a new directory");
                    System.out.println("deldir <dirname> - Delete a directory");
                    System.out.println("pwd - Print working directory");
                    System.out.println("create <filename> - Create a new file");
                    System.out.println("delfile <filename> - Delete a file");
                    System.out.println("help - Show this help message");
                    System.out.println("cls - Clear the prompt");
                    System.out.println("exit - Exit the shell");
                    break;
                default:
                    System.out.println(before + " > Error: Unknown command '" + command + "'");
                    break;
            }
        }
    }
}
