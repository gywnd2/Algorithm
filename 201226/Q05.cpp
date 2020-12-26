#include <iostream>
#include <cstring>
using namespace std;

int main()
{

    class Player
    {
    private:
        int xpos, ypos, squareSize;

    public:
        Player(int x, int y)
            : xpos(x), ypos(y)
        {
            cout << "Initial position : " << xpos << " " << ypos << endl;
        }

        void showCurrentPos()
        {
            cout << xpos << " " << ypos << endl;
            cout << "Size of square : " << squareSize << endl;
        }

        void goUp()
        {
            ypos += 1;
            cout << "Go Up!" << endl;
            showCurrentPos();
        }
        void goDown()
        {
            ypos -= 1;
            cout << "Go Down!" << endl;
            showCurrentPos();
        }
        void goLeft()
        {
            xpos -= 1;
            cout << "Go Left!" << endl;
            showCurrentPos();
        }
        void goRight()
        {
            xpos += 1;
            cout << "Go Right!" << endl;
            showCurrentPos();
        }

        void inputSquareSize(int num)
        {
            squareSize = num;
        }
        bool checkXboundary()
        {
            if (xpos < 1 || xpos > squareSize)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        bool checkYboundary()
        {
            if (ypos < 1 || ypos > squareSize)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
    };

    string moveInput;
    int N;
    cin >> N;
    cin.ignore();
    getline(cin, moveInput);
    for (int i = 0; i < moveInput.length(); i++)
    {
        if (moveInput[i] == ' ')
            moveInput.erase(i, 1);
    }

    Player p1(1, 1);
    p1.inputSquareSize(N);
    for (int i = 0; i < moveInput.length(); i++)
    {
        switch (moveInput.at(i))
        {
        case 'U':
            if (p1.checkYboundary() == true)
                p1.goUp();
            break;
        case 'R':
            if (p1.checkXboundary() == true)
                p1.goRight();
            break;
        case 'L':
            if (p1.checkXboundary() == true)
                p1.goLeft();
            break;
        case 'D':
            if (p1.checkYboundary() == true)
                p1.goDown();
            break;
        default:
            cout << "U, R, L, D 만 입력 가능합니다." << endl;
        }
    }

    p1.showCurrentPos();
}