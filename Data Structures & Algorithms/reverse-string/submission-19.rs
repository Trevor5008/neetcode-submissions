impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let tmp: Vec<char> = s.iter().rev().cloned().collect();
        for i in 0..s.len() {
            s[i] = tmp[i];
        }
    }
}
