// UVa 11498: Division of Nlogonia
#include <bits/stdc++.h>

using namespace std;

int main() {
    // INPUT
    while (true) {
        long long int K, Xborder, Yborder;
        cin >> K;  // No. testcases

        if (K == 0) break;

        cin >> Xborder >> Yborder;  // Division point

        // COMPUTATION & OUTPUT
        for (int i = 0; i < K; i++) {
            long long int X, Y;
            cin >> X >> Y;

            if ((X == Xborder) or (Y == Yborder)) cout << "divisa" << endl;
            else if ((X > Xborder) and (Y > Yborder)) cout << "NE" << endl;
            else if ((X > Xborder) and (Y < Yborder)) cout << "SE" << endl;
            else if ((X < Xborder) and (Y > Yborder)) cout << "NO" << endl;
            else if ((X < Xborder) and (Y < Yborder)) cout << "SO" << endl;
        }
    }

    return 0;
}