#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
  vector<string> grid;
  string line;
  while (getline(cin, line)) {
    grid.push_back(line);
  }

  ll X, Y, res = 0;
  char state;
  for (ll i = 0; i < grid.size(); ++i) {
    for (ll j = 0; j < grid.size(); ++j) {
      if (grid[i][j] == '^') {
        X = i, Y = j;
        state = grid[i][j];
        break;
      }
    }
  }

  char curr;
  while (X >= 0 && Y >= 0 && X < grid.size() && Y < grid.size()) {
    curr = grid[X][Y];

    if (curr != '#' && curr != 'X') {
      grid[X][Y] = 'X';
      res++;
    }

    if (curr == '#') {
      if (state == '^') {
        state = '>';
        X++;
      } else if (state == '>') {
        state = 'v';
        Y--;
      } else if (state == 'v') {
        state = '<';
        X--;
      } else if (state == '<') {
        state = '^';
        Y++;
      }
    }

    if (state == '^')
      X--;
    else if (state == '>')
      Y++;
    else if (state == 'v')
      X++;
    else if (state == '<')
      Y--;
  }

  cout << res << "\n";
}
