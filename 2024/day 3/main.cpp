#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll mul(const string &s) {
  regex mul_pattern(R"(mul\((\d+),(\d+)\))");
  sregex_iterator it(s.begin(), s.end(), mul_pattern);
  sregex_iterator end;

  ll res = 0;
  while (it != end) {
    smatch match = *it;
    int a = stoi(match[1]);
    int b = stoi(match[2]);
    res += (ll)a * b;
    ++it;
  }
  return res;
}

ll solve_part1(const string &s) { return mul(s); }

ll solve_part2(const string &s) {
  regex split_pattern(R"(don't|do)");
  sregex_token_iterator it(s.begin(), s.end(), split_pattern, {-1, 0});
  sregex_token_iterator end;

  ll res = 0;
  bool mul_enabled = true;

  while (it != end) {
    string input = *it++;
    if (input == "do") {
      mul_enabled = true;
    } else if (input == "don't") {
      mul_enabled = false;
    } else {
      if (mul_enabled) {
        res += mul(input);
      }
    }
  }

  return res;
}

int main() {
  ifstream input_file("./input.txt");
  if (!input_file) {
    cout << "could not open file\n";
    return 1;
  }
  string input((istreambuf_iterator<char>(input_file)),
               istreambuf_iterator<char>());

  cout << solve_part1(input) << " ";
  cout << solve_part2(input) << "\n";

  return 0;
}
