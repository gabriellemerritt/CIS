#ifndef MAGICSQUARE2_H
#define MAGICSQUARE2_H
#define MAGICSIZE 3 

typedef int MSQUARE_TYPE[MAGICSIZE][MAGICSIZE]; 
typedef MSQUARE_TYPE *MagSquare_PTR; 
void initSquare(MSQUARE_TYPE MagSquare_PTR, int magicsquaresize); 
void printSquare(MSQUARE_TYPE MagSquare_PTR, int magicsquaresize); 
int sumColumn (int column, MSQUARE_TYPE MagSquare_PTR, int size); 
int sumRow(int row, MSQUARE_TYPE MagSquare_PTR, int size); 
int sumDiagonal(int diagonal, MSQUARE_TYPE MagSquare_PTR, int size);
int isMagic(MSQUARE_TYPE MagSquare_PTR, int size);
void testMagic (MSQUARE_TYPE MagSquare_PTR);
void permuteSquare(MSQUARE_TYPE MagSquare_PTR);
#endif // MAGICSQUARE2_H