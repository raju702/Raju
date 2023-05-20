package Pratice;
public class PascalTriangle {
    private static int[][] cache;

    public static void main(String[] args) {
        int numRows = 10; //Number of rows in Pascal's triangle

        // Initialize cache
        cache = new int[numRows + 1][numRows + 1];
        for (int i = 0; i <= numRows; i++) {
            for (int j = 0; j <= numRows; j++) {
                cache[i][j] = -1;
            }
        }

        System.out.println("Pascal's Triangle (Memoization):");
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col <= row; col++) {
                int coefficient = pascalMemoization(row, col);
                System.out.print(coefficient + " ");
            }
            System.out.println();
        }
    }

    private static int pascalMemoization(int row, int col) {
        if (cache[row][col] != -1) {
            return cache[row][col];
        }

        if (col == 0 || col == row) {
            cache[row][col] = 1;
        } else {
            cache[row][col] = pascalMemoization(row - 1, col - 1) + pascalMemoization(row - 1, col);
        }

        return cache[row][col];
    }
}
