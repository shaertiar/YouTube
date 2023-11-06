import java.util.Random;

public class RockPaperScissor {
	// All of the choice that a computer can choice
	private static final String[] computerChoices = {"Rock", "Paper", "Scissor"};

	public String getComputerChoice() {
		return computerChoice;
	}
	public int getComputerScore() {
		return computerScore;
	}
	public int getPlayerScore() {
		return playerScore;
	}

	// Store the computer choice
	private String computerChoice;

	//Store the scores
	private int computerScore, playerScore;

	// Use to generate a random number to randomly choose an option for the computer
	private Random random;

	// Constructor for init rand obj
	public RockPaperScissor() {
		random = new Random();
	}

	// Begin playing rook paper or scissor
	public String playRockPaperScissor(String playerChoice) {
		// Generate computer choice
		computerChoice = computerChoices[random.nextInt(computerChoices.length)];

		// Result
		String result;

		// Evaluate the winner
		if (computerChoice.equals("Rock")) {
			if (playerChoice.equals("Paper")) {
				result = "Player Wins";
				playerScore++;
			} else if (playerChoice.equals("Scissors")) {
				result = "Computer Wins";
				computerScore++;
			} else {
				result = "Draw";
			}
		} else if (computerChoice.equals("Paper")) {
			if (playerChoice.equals("Scissors")) {
				result = "Player Wins";
				playerScore++;
			} else if (playerChoice.equals("Rock")) {
				result = "Computer Wins";
				computerScore++;
			} else {
				result = "Draw";
			}
		} else {
			if (playerChoice.equals("Rock")) {
				result = "Player Wins";
				playerScore++;
			} else if (playerChoice.equals("Paper")) {
				result = "Computer Wins";
				computerScore++;
			} else {
				result = "Draw";
			}
		}

		return result;
	}
}