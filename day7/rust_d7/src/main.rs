use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::{SystemTime};

struct Row
{
    target: i64,
    values: Vec<i64>
}

fn fill_rows(rows: &mut Vec<Row>)
{
    // File hosts.txt must exist in the current path
    //if let Ok(lines) = read_lines("../input/example.txt")
    if let Ok(lines) = read_lines("../input/data.txt")
    {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten()
        {
            //println!("{}", line);
            let mut s = String::new();
            let mut row = Row 
                {
                    target: 0,
                    values: Vec::new(),
                };

            for x in line.chars()
            {
                if x == ':'
                {
                    row.target = s.parse::<i64>().unwrap();
                    s.clear();
                }
                else if x == ' '
                {
                    if s.len() > 0
                    {
                        row.values.push(s.parse::<i64>().unwrap());
                        s.clear();
                    }
                }
                else
                {
                    s.push(x);
                }
            }
            row.values.push(s.parse::<i64>().unwrap());
            rows.push(row);
        }
    }
}

fn get_num_digits(x:i64)->u32
{
    let mut digits:u32 = 0;
    let mut x = x;
    while x != 0
    {
        digits += 1;
        x = x / 10;
    }
    return digits
}

fn concat(a:i64, b:i64)->i64
{
    return a * i64::pow(10, get_num_digits(b)) + b;
}

fn encode_operators(key:u32, length:u32, factor: u32)->Vec<u32>
{
    let mut key = key;
    let mut ops: Vec<u32> = Vec::new();
    for _i in 0..length
    {
        ops.push(key % factor);
        key = key / factor;
    }
    return ops;
}

fn calculate_solution(values: Vec<i64>, ops: Vec<u32>)->i64
{
    let mut soln: i64 = values[0];
    for i in 0..ops.len()
    {
        match ops[i]
        {
            0 => soln += values[i+1],
            1 => soln *= values[i+1],
            2 => soln = concat(soln, values[i+1]),
            _ => soln = soln,
        }
    }
    return soln;
}

fn get_cal_total(row: &Row, factor: u32)->i64
{
    let max:u32 = row.values.len() as u32 - 1;
    let values = &row.values;
    let length:u32= values.len() as u32 - 1;
    for key in 0..factor.pow(max)
    {
        let ops: Vec<u32> = encode_operators(key, length, factor);
        let soln: i64 = calculate_solution(values.clone(), ops);
        if soln == row.target
        {
            //println!("Found: {}",row.target);
            return row.target;
        }
    }
    return 0;   
}

fn main()
{
    let time = SystemTime::now();
    let mut rows: Vec<Row> = Vec::new();
    fill_rows(&mut rows);
    //println!("{} : {:?}",rows[0].target, rows[0].values);

    let mut cal_total_p1:i64 = 0;
    let mut cal_total_p2:i64 = 0;

    for row in rows
    {
        cal_total_p1 += get_cal_total(&row, 2);
        cal_total_p2 += get_cal_total(&row, 3);
    }
    println!("Solution 1 calibration total is: {cal_total_p1}");
    println!("Solution 2 calibration total is: {cal_total_p2}");
    println!("Execution Time: {:?}", time.elapsed());
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
