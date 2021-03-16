#include <iostream>

int BinSearch(int ar[], int len, int target)
{
    int first = 0;
    int last = len - 1;
    int mid;

    while (first <= last)
    {
        mid = (first + last) / 2;

        if (target == ar[mid])
        {
            return mid;
        }

        else
        {
            if (target < ar[mid])
            {
                last = mid - 1;
            }
            else
            {
                first = mid + 1;
            }
        }
    }

    return -1;
}

int main()
{
    int arr[] = {1, 3, 5, 7, 9};
    int index;

    index = BinSearch(arr, sizeof(arr) / sizeof(int), 7);
    if (index == -1)
        std::cout << "Å½»ö ½ÇÆĞ" << std::endl;

    else
        std::cout << "Å¸°Ù ÀúÀå ÀÎµ¦½º: " << index << std::endl;

    index = BinSearch(arr, sizeof(arr) / sizeof(int), 4);

    if (index == -1)
        std::cout << "Å½»ö ½ÇÆĞ" << std::endl;
    else
        std::cout << "Å¸°Ù ÀúÀå ÀÎµ¦½º: " << index << std::endl;

    return 0;
}