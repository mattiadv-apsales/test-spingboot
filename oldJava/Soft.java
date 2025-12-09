package oldJava;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Main {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Quadrato muovibile con WASD");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Coordinate iniziali del quadrato
        final int[] x = {(frame.getWidth() - 100) / 2};
        final int[] y = {(frame.getHeight() - 100) / 2};

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.BLUE);
                g.fillRect(x[0], y[0], 100, 100);
            }
        };

        // Listener per i tasti
        frame.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                int step = 10; // passi di movimento
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_W -> y[0] -= step; // su
                    case KeyEvent.VK_S -> y[0] += step; // giù
                    case KeyEvent.VK_A -> x[0] -= step; // sinistra
                    case KeyEvent.VK_D -> x[0] += step; // destra
                }
                panel.repaint(); // ridisegna il quadrato
            }
        });

        frame.add(panel);
        frame.setVisible(true);
        frame.setFocusable(true); // importante per ricevere input da tastiera
        frame.requestFocusInWindow();
    }
}