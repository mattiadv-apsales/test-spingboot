package oldJava;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage stage) {
        // Bottone semplice
        Button btn = new Button("Cliccami!");
        btn.setOnAction(e -> System.out.println("Hai cliccato il bottone!"));

        // Layout base
        StackPane root = new StackPane(btn);

        // Scene
        Scene scene = new Scene(root, 300, 200);

        // Stage (finestra)
        stage.setTitle("Minimal JavaFX App");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
