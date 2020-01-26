from typing import Dict, List, Tuple

class Interval:

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __lt__(self, other):
        return self.finish < other.finish

    def do_not_intersect(self, other):
        return other.start >= self.finish

    def __repr__(self):
        return "({}, {})".format(self.start, self.finish)


def greedy_job_scheduling(intervals: List[Interval]):
    """
    Maximizing the number of jobs scheduled
    :param intervals: list of jobs
    :return: list of jobs
    """
    sorted_intervals = sorted(intervals)
    optimal_jobs = []
    num_jobs = 0
    for job in sorted_intervals:
        if optimal_jobs == [] or optimal_jobs[num_jobs - 1].do_not_intersect(job):
            optimal_jobs.append(job)
            num_jobs += 1


    return optimal_jobs


def create_intervals(intervals_list):
    intervals = []
    for i in intervals_list:
        intervals.append(Interval(i[0], i[1]))
    return intervals

if __name__ == '__main__':
    intervals = [(1, 3), (2, 4), (3, 5), (6, 7)]
    print(greedy_job_scheduling(create_intervals(intervals)))