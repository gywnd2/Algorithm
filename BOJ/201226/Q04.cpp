/*
1�� �� �� ����
� �� N�� 1�� �� �� ����
1. N���� 1�� ���ų�
2. N�� K�� ���� �� �ִ�.
�� ���� Ƚ���� ī��Ʈ �ϰ� �־�� �ϸ� 2�� ������ N�� K�� ������ ������ ����
�����ϴ�.
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

        if (res % K == 0) //res���� N�� �ϸ� ��� N�� 25�� �����̱� ������ ���ѷ����� ����
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