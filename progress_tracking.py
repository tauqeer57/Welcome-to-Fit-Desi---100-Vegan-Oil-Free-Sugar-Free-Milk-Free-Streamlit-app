# progress_tracking.py

class ProgressTracker:
    def __init__(self):
        self.weight_log = []
        self.measurements_log = []

    def log_weight(self, weight: float):
        """Log user's weight."""
        self.weight_log.append(weight)

    def log_measurements(self, measurements: dict):
        """Log user's body measurements."""
        self.measurements_log.append(measurements)

    def get_progress(self):
        """Return user's progress."""
        return {
            "weight": self.weight_log,
            "measurements": self.measurements_log
        }
