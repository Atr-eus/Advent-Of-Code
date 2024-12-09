#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Block {
  ll beg;
  ll len;
  ll id;

public:
  Block(ll a, ll b, ll c = -1) : beg(a), len(b), id(c) {};
  void display() { cout << "{ " << beg << ", " << len << ", " << id << " }\n"; }
  ll start() { return beg; }
  ll length() { return len; }
  ll ID() { return id; }
  void set_start(ll s) { beg = s; };
  void set_length(ll l) { len = l; };
};

int main() {
  char dig;
  ll n, file_id, part1, part2;
  file_id = part1 = part2 = 0;
  bool free_turn = false;
  vector<ll> disk;
  vector<Block> file_blocks;
  vector<Block> free_blocks;

  while ((dig = getchar()) != EOF) {
    n = dig - '0';

    if (free_turn) {
      free_blocks.push_back(Block(disk.size(), n));
      for (ll i = 0; i < n; ++i)
        disk.push_back(-1);
    } else {
      file_blocks.push_back(Block(disk.size(), n, file_id));
      for (ll i = 0; i < n; ++i)
        disk.push_back(file_id);

      file_id++;
    }

    free_turn = !free_turn;
  }

  for (ll i = 0; i < disk.size(); ++i) {
    if (disk[i] == -1) {
      swap(disk[i], disk[disk.size() - 1]);

      while (disk[disk.size() - 1] == -1) {
        disk.pop_back();
      }
    }
    part1 += disk[i] * i;
  }

  // for (auto i : disk)
  //   cout << i << " ";
  // cout << "\n";
  // for (auto i : file_blocks)
  //   i.display();
  // cout << "\n";
  // for (auto i : free_blocks)
  //   i.display();
  // cout << "\n";

  while (file_blocks.size()) {
    Block &file_block = file_blocks[file_blocks.size() - 1];

    for (auto &free_block : free_blocks) {
      if (file_block.start() > free_block.start() &&
          file_block.length() <= free_block.length()) {
        file_block.set_start(free_block.start());
        free_block.set_length(free_block.length() - file_block.length());
        free_block.set_start(free_block.start() + file_block.length());

        break;
      }
    }

    for (ll i = 0; i < file_block.length(); ++i) {
      part2 += (file_block.start() + i) * file_block.ID();
    }
    file_blocks.pop_back();
  }

  cout << part1 << " ";
  cout << part2 << "\n";
}
