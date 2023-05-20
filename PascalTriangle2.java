package Pratice;

public class PascalTriangle2 {
    public static void main(String[] args) {
	        int numRows = 7; // Number of rows in Pascal's triangle

	        System.out.println("Pascal's Triangle (Recursion):");
	        for (int row = 0; row < numRows; row++) {
	            for (int col = 0; col <= row; col++) {
	                int coefficient = pascalRecursion(row, col);
	                System.out.print(coefficient + " ");
	            }
	            System.out.println();
	        }
	    }

	    private static int pascalRecursion(int row, int col) {
	        if (col == 0 || col == row) {
	            return 1;
	        } else {
	            return pascalRecursion(row - 1, col - 1) + pascalRecursion(row - 1, col);
	        }
	    }
	}

