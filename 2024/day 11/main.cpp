#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dig_c(ll n) {
  if (n == 0)
    return 0;
  else
    return 1 + dig_c(n / 10);
}

pair<ll, ll> div_dig(ll n) {
  string sn = to_string(abs(n));
  string l = sn.substr(0, sn.size() / 2);
  string r = sn.substr(sn.size() / 2);

  return {stoll(l), stoll(r)};
}

ll part1(vector<ll> &st) {
  for (ll i = 0; i < 25; ++i) {
    for (ll j = 0; j < st.size();) {
      if (st[j] == 0) {
        st[j] = 1;
        j++;
      } else if (!(dig_c(st[j]) & 1)) {
        auto [lsub, rsub] = div_dig(st[j]);
        st.erase(st.begin() + j);
        st.insert(st.begin() + j, {lsub, rsub});
        j += 2;
      } else {
        st[j] *= 2024;
        j++;
      }
    }
  }

  return st.size();
}

int main() {
  vector<ll> st;
  ll n;
  while (scanf("%lld", &n) == 1) {
    st.emplace_back(n);
  }
  cout << part1(st) << "\n";
}
