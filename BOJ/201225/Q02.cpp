/*
ū���� ��Ģ
�־��� ������ M�� ���Ͽ� ���� ū ���� �����, ���� ���Ұ� K���̻� ������ �� ����.
��, �ٸ� ���Ҹ� �ѹ� ���ϰ� �� �ٽ� K�� ���ϴ� ������ ������ ���ϴ� ���� ����.
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, M, K;
    int result = 0;
    string strInput;
    vector<int> vecNum;

    cin >> N >> M >> K;
    cout << "�迭 �Է� : ";
    cin.ignore(); // ���ۿ� ���๮�ڰ� ���� �ֱ� ������ ignore => ������ �� ���ڸ� ���ۿ��� �о��ִ� �׷��Լ�
    getline(cin, strInput);

    string strNum = "";
    for (int i = 0; i < strInput.length(); i++)
    {
        if (strInput.at(i) == ' ')
        {
            vecNum.push_back(atoi(strNum.c_str()));
            strNum = "";
        }

        else
        {
            strNum += strInput.at(i);
            continue;
        }
    }
    vecNum.push_back(atoi(strNum.c_str()));

    sort(vecNum.rbegin(), vecNum.rend());

    int i = 1;
    int j = 1;
    int idx = 0;

    while (i <= M)
    {
        for (j; i <= M && j <= K; j++)
        {
            if (i < M)
            {
                result += vecNum[idx];
                cout << "adding : " << vecNum[idx] << endl;
                i++;
            }
        }

        /*
        46 ���� i<M�� �־�� i/j�� 8/2�� ��Ȳ�� �Ǿ����� �� ������� ���� �����Ƿ�
        ���� �� �ִ�. ������ j�� ���� ���� �ʾ����Ƿ� �ѹ� �� �����ϰ� �׶�
        �Ѵ� �����Ѵٴ� ���ǿ� ���� ���� �����Ƿ� ������ �Ǿ� ���� Ʋ��.
        ||�� ���� i�� M�� �����Ҷ� ���� ������ ��Ģ�� ��� �����ϰ� ����.
         */

        result += vecNum[idx + 1];
        cout << "adding : " << vecNum[idx + 1] << endl;
        i++;
        j = 1;

        cout << "i : " << i << endl;
    }

    cout << result << endl;
}