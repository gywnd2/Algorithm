#include <iostream>
using namespace std;

void selSort(int arr[], int n)
{ // arr를 parameter로 넘겨주면 시작 주소값을 넘겨주기 때문에 for문에서 sizeof(arr)/sizeof(int)를 직접 사용할 수 없다
    int i, j, min, temp;

    for (i = 0; i < n - 1; i++)
    {
        min = i;
 
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min])
                min = j;
        }

        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

int main()
{
    int arr[4] = {3, 4, 2, 1};
    int i;

    selSort(arr, sizeof(arr) / sizeof(int));

    for (i = 0; i < 4; i++)
    {
        cout << arr[i] << endl;
    }

    return 0;
}