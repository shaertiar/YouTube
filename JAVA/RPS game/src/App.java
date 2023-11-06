import javax.swing.*;

public class App {
	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() {
			@Override
			public void run() {
				// Instantable a RPSGUI
				RockPaperScissorGUI rockpaperScossorGUI = new RockPaperScissorGUI();

				// Display the GUI
				rockpaperScossorGUI.setVisible(true);
			}
		});
	}
}