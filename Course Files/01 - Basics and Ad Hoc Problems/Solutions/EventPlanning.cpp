// UVa 11559: Event Planning
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ll N = 1, B = 1, H = 1, W = 1;  // No. participants, budget, No hotels and No weeks.
    ll testCases;
    cin >> testCases;

    while (scanf("%lld %lld %lld %lld", &N, &B, &H, &W) != EOF) {

        ll minCost = 10000000;  // Minimum cost for spending, this exceeds the max possible value of 200 * 10000 = 2000000.

        for (ll i = 0; i < H; i++) {
            ll hotelPrice;
            cin >> hotelPrice;

            for (ll j = 0; j < W; j++) {
                ll available;  // No. of available rooms
                cin >> available;

                // If Hi >= N, move on
                if (available >= N) {
                    // If N * P <= B, move on
                    if (N * hotelPrice <= B) {
                        // Minimum cost will be the lower amount
                        minCost = min(minCost, N * hotelPrice);
                    }
                }
            }
        }

        // Check if can output
        if (minCost == 10000000) {
            printf("stay home\n");
        } else {
            printf("%lld\n", minCost);
        }
    }

    return 0;
}