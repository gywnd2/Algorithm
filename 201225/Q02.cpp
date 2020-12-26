/*
큰수의 법칙
주어진 수들을 M번 더하여 가장 큰 수를 만들되, 같은 원소가 K번이상 더해질 수 없다.
단, 다른 원소를 한번 더하고 또 다시 K번 더하는 식으로 번갈아 더하는 것은 가능.
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
    cout << "배열 입력 : ";
    cin.ignore(); // 버퍼에 개행문자가 남아 있기 때문에 ignore => 마지막 한 문자를 버퍼에서 털어주는 그런함수
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
        46 행의 i<M을 넣어야 i/j가 8/2인 상황이 되었을때 총 연산수를 충족 했으므로
        멈출 수 있다. 없으면 j가 충족 되지 않았으므로 한번 더 수행하고 그때
        둘다 만족한다는 조건에 충족 하지 않으므로 끝나게 되어 값이 틀림.
        ||을 쓰면 i가 M에 도달할때 까지 문제의 규칙을 모두 무시하고 더함.
         */

        result += vecNum[idx + 1];
        cout << "adding : " << vecNum[idx + 1] << endl;
        i++;
        j = 1;

        cout << "i : " << i << endl;
    }

    cout << result << endl;
}