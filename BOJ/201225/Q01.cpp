/* 201225 Q01 
   10�� ��� �ݾ��� �Է� �޾� 500, 100, 50, 10�� ¥�� ������ �ּҰ����� ���� ���ϴ� ����
*/

#include <iostream>
using namespace std;

int num, rem1, rem2, rem3, rem4, num500, num100, num50, num10, numcoin;

int main(){
    cout<<"10�� ��� �Է� : ";
    cin>>num;

    num500=num/500;
    rem1=num-(500*num500);
    num100=rem1/100;
    rem2=rem1-(100*num100);
    num50=rem2/50;
    rem3=rem2-(50*num50);
    num10=rem3/10;
    rem4=rem3-(10*num10);

    numcoin=num500+num100+num50+num10;

    cout<<"������ �ּҰ��� : "<<numcoin<<endl;
}