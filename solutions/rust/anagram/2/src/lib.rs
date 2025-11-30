use itertools::Itertools;
use std::collections::HashSet;
use unicode_segmentation::UnicodeSegmentation;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    possible_anagrams
        .iter()
        .filter(|anagram| is_anagram_of(word, anagram))
        .filter(|anagram| word.to_lowercase() != anagram.to_lowercase())
        .copied()
        .collect()
}

fn is_anagram_of(word: &str, potential_anagram: &str) -> bool {
    sanitize(word) == sanitize(potential_anagram)
}

fn sanitize(word: &str) -> String {
    word.to_lowercase().graphemes(true).sorted().collect()
}
