/* 201225 Q01 
   10의 배수 금액을 입력 받아 500, 100, 50, 10원 짜리 동전의 최소개수의 합을 구하는 문제
*/

#include <iostream>
using namespace std;

int num, rem1, rem2, rem3, rem4, num500, num100, num50, num10, numcoin;

int main(){
    cout<<"10의 배수 입력 : ";
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

    cout<<"동전의 최소개수 : "<<numcoin<<endl;
}