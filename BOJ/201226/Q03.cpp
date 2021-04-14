/*
숫자 카드 게임
N by M 크기의 숫자 카드들이 있다. 각 행에서 가장 작은 카드들을 모아 그 카드들 중
가장 큰 카드의 수를 출력하는 문제
*/

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N = 0;
    int M = 0;
    int row, column;
    cin >> N >> M;
    int Card[N][M];
    int rowMin[N];
    int minSum = 0;
    int maxOfRows=0;

    for (row = 0; row < N; row++)
    {
        for (column = 0; column < M; column++)
        {
            cin >> Card[row][column];
        }
    }

    cout << endl;

    for (row = 0; row < N; row++)
    {
        int min = Card[row][0];

        for (column = 0; column < M; column++)
        {
            if (min >= Card[row][column]) // =를 빼먹어서 안됬었음
            {
                min = Card[row][column];
                rowMin[row] = min;
            }
        }
    }

    for (row = 0; row < N; row++) 
    {
        maxOfRows=0;
        if(maxOfRows<=rowMin[row]){
            maxOfRows=rowMin[row];
            minSum=maxOfRows;
        }
    }

    cout << minSum << endl;
}
