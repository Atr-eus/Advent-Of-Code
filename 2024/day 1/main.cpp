#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
  ifstream inputFile("input.txt");
  if (!inputFile) {
    cout << "could not open file\n";
    return 1;
  }

  vector<ll> a, b;
  ll n1, n2, res = 0;
  while (inputFile >> n1 >> n2) {
    a.push_back(n1);
    b.push_back(n2);
  }
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  for (ll i = 0; i < a.size(); ++i) {
    res += abs(b[i] - a[i]);
  }
  cout << res << "\n";
}
