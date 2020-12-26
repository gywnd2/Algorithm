/*
1이 될 때 까지
어떤 수 N이 1이 될 때 까지
1. N에서 1을 빼거나
2. N을 K로 나눌 수 있다.
단 연산 횟수를 카운트 하고 있어야 하며 2번 연산은 N이 K로 나누어 떨어질 때만
가능하다.
*/

#include <iostream>
using namespace std;

int main()
{
    int N, K, res;
    int count = 0;

    cin >> N >> K;

    res = N;

    do
    {

        if (res % K == 0) //res말고 N을 하면 계속 N은 25로 고정이기 때문에 무한루프에 빠짐
        {
            res /= K;
            count++;
        }

        else
        {
            res -= 1;
            count++;
        }

    } while (res != 1);

    cout << count << endl;
}