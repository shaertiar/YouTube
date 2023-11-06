import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RockPaperScissorGUI extends JFrame implements ActionListener  {
	// PLayer buttons
	JButton rockButton, paperButton, scissorButton;

	// Will display the choice of the computer
	JLabel computerChoice;

	// Will display the score
	JLabel computerScoreLabel, playerScoreLabel;

	// Backend obj
	RockPaperScissor rookPaperScissor;

	public RockPaperScissorGUI() {
		// Title app
		super("Rock Paper Scissors");

		// Set window size
		setSize(450, 574);
		setResizable(false);

		// Set layout to null
		setLayout(null);

		// Close java when close app
		setDefaultCloseOperation(EXIT_ON_CLOSE);

		// Load GUI to center
		setLocationRelativeTo(null);

		// Init backend
		rookPaperScissor = new RockPaperScissor();

		// Add GUI components
		addGuiComponents();
	}

	private void addGuiComponents() {
		// Create computer score label
		computerScoreLabel = new JLabel("Computer: 0");

		// Set x, y, width, height val
		computerScoreLabel.setBounds(0, 43, 450, 30);

		// Set font
		computerScoreLabel.setFont(new Font("Dialog", Font.BOLD, 26));

		// Place text to center
		computerScoreLabel.setHorizontalAlignment(SwingConstants.CENTER);

		// Add to GUI
		add(computerScoreLabel);

		// Create computer choice
		computerChoice = new JLabel("?");
		computerChoice.setBounds(175, 118, 98, 81);
		computerChoice.setFont(new Font("Dialog", Font.PLAIN, 18));
		computerChoice.setHorizontalAlignment(SwingConstants.CENTER);
		// Create a black border around
		computerChoice.setBorder(BorderFactory.createLineBorder(Color.black));
		add(computerChoice);

		// Create a player score label
		playerScoreLabel = new JLabel("Player: 0");
		playerScoreLabel.setBounds(0, 317, 450, 30);
		playerScoreLabel.setFont(new Font("Dialog", Font.BOLD, 26));
		playerScoreLabel.setHorizontalAlignment(SwingConstants.CENTER);
		add(playerScoreLabel);

		// Rock button
		rockButton = new JButton("Rock");
		rockButton.setBounds(40, 387, 105, 81);
		rockButton.setFont(new Font("Dialog", Font.PLAIN, 18));
		rockButton.addActionListener(this);
		add(rockButton);

		// Paper button
		paperButton = new JButton("Paper");
		paperButton.setBounds(165, 387, 105, 81);
		paperButton.setFont(new Font("Dialog", Font.PLAIN, 18));
		paperButton.addActionListener(this);
		add(paperButton);

		// Scissor button
		scissorButton = new JButton("Scissor");
		scissorButton.setBounds(290, 387, 105, 81);
		scissorButton.setFont(new Font("Dialog", Font.PLAIN, 18));
		scissorButton.addActionListener(this);
		add(scissorButton);
	}

	// Display a message dialog which will show the winner and a try again button to play again
	private void showDialog(String message) {
		JDialog resultDialog = new JDialog(this, "Result", true);
		resultDialog.setSize(227, 124);
		resultDialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		resultDialog.setResizable(false);

		// Message label
		JLabel resultLabel = new JLabel(message);
		resultLabel.setFont(new Font("Dialog", Font.BOLD, 18));
		resultLabel.setHorizontalAlignment(SwingConstants.CENTER);
		resultDialog.add(resultLabel, BorderLayout.CENTER);

		// Try again button
		JButton tryAgainButton = new JButton("Try again?");
		tryAgainButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// Reset computer choice
				computerChoice.setText("?");

				// Close the display box
				resultDialog.dispose();
			}
		});
		resultDialog.add(tryAgainButton, BorderLayout.SOUTH);

		resultDialog.setLocationRelativeTo(this);
		resultDialog.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// Get player choice
		String playerChoice = e.getActionCommand().toString();

		// Play rock paper scissor, and store result into str var
		String result = rookPaperScissor.playRockPaperScissor(playerChoice);

		// Load computer choice
		computerChoice.setText(rookPaperScissor.getComputerChoice());

		// Update score
		computerScoreLabel.setText("Computer: " + rookPaperScissor.getComputerScore());
		playerScoreLabel.setText("Player: " + rookPaperScissor.getPlayerScore());

		// Display result dialog
		showDialog(result);
	}
}