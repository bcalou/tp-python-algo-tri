import time

def count_time():
    """Count time:
    Simple method to count time between the start and end of an operation"""
    start: float = time.time()
    # do something
    end: float = time.time()
    print("Temps écoulé :", end - start)
