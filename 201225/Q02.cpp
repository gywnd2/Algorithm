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
    cin.ignore();
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
        for (; j <= K && i < M; j++) // �� i<=M �̸� ���� �ȳ�����? �� 583 24546�� ������ ������ �Ȱ��� 572 34343�� ���� �ٸ���?
        {
            result += vecNum[idx];
            cout << "adding : " << vecNum[idx] << endl;
            i++;
        }

        result += vecNum[idx + 1];
        cout << "adding : " << vecNum[idx + 1] << endl;
        i++;
        j = 1;

        cout << "i : " << i << endl;
    }

    cout << result << endl;
}