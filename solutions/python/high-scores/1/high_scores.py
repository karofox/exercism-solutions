class HighScores:
    """High Scores table.
    
    scores: list of scores.
    """
    def __init__(self, scores: list[int]):
        self.scores = scores

    def latest(self) -> int:
        """Return the latest score."""
        return self.scores[-1]
    
    def personal_best(self) -> int:
        """Return the personal best score."""
        return max(self.scores)
    
    def personal_top_three(self) -> int:
        """Return top three scores."""
        return sorted(self.scores.copy(), reverse=True)[:3]