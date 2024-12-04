use std::io::{self, BufRead};

fn solve_part1(input: &Vec<Vec<char>>) -> u32 {
    let mut res: u32 = 0;

    for i in 0..input.len() {
        for j in 0..input[0].len() {
            for (x, y) in &[
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
                (1, -1),
                (-1, 1),
                (1, 1),
                (-1, -1),
            ] {
                if (0..4).all(|k| {
                    let X = i as isize + x * k;
                    let Y = j as isize + y * k;

                    X >= 0
                        && X < input.len() as isize
                        && Y >= 0
                        && Y < input[0].len() as isize
                        && input[X as usize][Y as usize] == "XMAS".chars().nth(k as usize).unwrap()
                }) {
                    res += 1;
                }
            }
        }
    }

    res
}

fn solve_part2(input: &Vec<Vec<char>>) -> u32 {
    let mut res: u32 = 0;

    for i in 1..(input.len() - 1) {
        for j in 1..(input.len() - 1) {
            if input[i][j] == 'A' {
                if (input[i - 1][j - 1] == 'M'
                    && input[i + 1][j + 1] == 'S'
                    && input[i - 1][j + 1] == 'M'
                    && input[i + 1][j - 1] == 'S')
                    || (input[i - 1][j - 1] == 'M'
                        && input[i + 1][j + 1] == 'S'
                        && input[i + 1][j - 1] == 'M'
                        && input[i - 1][j + 1] == 'S')
                    || (input[i + 1][j + 1] == 'M'
                        && input[i - 1][j - 1] == 'S'
                        && input[i - 1][j + 1] == 'M'
                        && input[i + 1][j - 1] == 'S')
                    || (input[i + 1][j + 1] == 'M'
                        && input[i - 1][j - 1] == 'S'
                        && input[i + 1][j - 1] == 'M'
                        && input[i - 1][j + 1] == 'S')
                {
                    res += 1;
                }
            }
        }
    }

    res
}

fn main() {
    let mut input: Vec<Vec<char>> = Vec::new();
    for line in io::stdin().lock().lines() {
        match line {
            Ok(l) => input.push(l.chars().collect()),
            Err(why) => eprintln!("ERROR: {}", why),
        }
    }

    println!("{}", solve_part1(&input));
    println!("{}", solve_part2(&input));
}

// rustc main.rs
// cat input.txt | ./main
