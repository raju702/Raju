package Pratice;

public class PascalTriangle3 {
	    public static void main(String[] args) {
	        int numRows = 7; // Number of rows in Pascal's triangle

	        System.out.println("Pascal's Triangle (Iteration):");
	        for (int row = 0; row < numRows; row++) {
	            for (int col = 0; col <= row; col++) {
	                int coefficient = pascalIteration(row, col);
	                System.out.print(coefficient + " ");
	            }
	            System.out.println();
	        }
	    }

	    private static int pascalIteration(int row, int col) {
	        int coefficient = 1;
	        for (int i = 1; i <= col; i++) {
	            coefficient = coefficient * (row - i + 1) / i;
	        }
	        return coefficient;
	    }
	}

