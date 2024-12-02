#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll solve_part1(vector<ll> &a, vector<ll> &b) {
  ll res = 0;

  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  for (ll i = 0; i < a.size(); ++i) {
    res += abs(b[i] - a[i]);
  }

  return res;
}

ll solve_part2(vector<ll> &a, vector<ll> &b) {
  ll res = 0, factor;
  for (ll i = 0; i < a.size(); ++i) {
    factor = 0;
    for (ll j = 0; j < b.size(); ++j) {
      if (a[i] == b[j])
        factor++;
    }

    res += factor * a[i];
  }

  return res;
}

int main() {
  ifstream input("input.txt");
  if (!input) {
    cout << "could not open file\n";
    return 1;
  }

  vector<ll> a, b;
  ll n1, n2;
  while (input >> n1 >> n2) {
    a.push_back(n1);
    b.push_back(n2);
  }

  cout << solve_part1(a, b) << " ";
  cout << solve_part2(a, b) << "\n";

  input.close();
  return 0;
}
