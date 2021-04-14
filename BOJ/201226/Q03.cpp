/*
���� ī�� ����
N by M ũ���� ���� ī����� �ִ�. �� �࿡�� ���� ���� ī����� ��� �� ī��� ��
���� ū ī���� ���� ����ϴ� ����
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
            if (min >= Card[row][column]) // =�� ���Ծ �ȉ����
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
