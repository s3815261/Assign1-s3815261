import random
import time
import sys


class DataGenerator:
    # Program name.
    prog_name = "DataGenerator"

    def __init__(self, start_of_range, end_of_range, sampleData, sampleSize, ):
        # Start of integer range to generate values from.
        self.start_of_range = start_of_range
        # End of integer range to generate values from.
        self.end_of_range = end_of_range
        # Random generator to use.
        random.seed(time.time())
        # Sample dataset to use
        # self.sampleData =


def sample_without_replacement(self, samples_len):
    """
    Sample without replacement, using "Algorithm R" by Jeffrey Vitter, in paper "Random sampling without a reservoir".
    This algorithm has O(size of range) time complexity.

    @param samples_len Number of samples to generate.
    @throws IllegalArgumentException When samples_len is greater than the valid integer range.
    """
    population_size = self.end_of_range - self.start_of_range + 1

    if samples_len > population_size:
        raise ValueError("samples_len cannot be greater than population_size for sampling without replacement.");

    samples = []
    # fill it with initial values in the range
    for i in range(samples_len):
        samples.append(i + self.start_of_range)

    # replace
    for j in range(samples_len, population_size):
        t = random.randint(0, j + 1)
        if t < samples_len:
            samples[t] = j + self.start_of_range
    return samples


def main():
    # check correct number of command line arguments
    args = sys.argv[1:]
    if len(args) != 4:
        DataGenerator.usage()

    try:
        # Get sampleData file
        sampleData = str(args[0])
        # Size of samples of words to produce e.g 1k, 2k, 5k
        sampleSize = int(args[1])
        # What operation to test
        operation = str(args[2])
        # Name of output file
        output = str(args[3])

        # number of values to sample
        samples_len = int(args[2])

        # type of sampling
        sampling_type = args[3]

        start_of_range = 1
        end_of_range = 200 * 1000

        gen = DataGenerator(start_of_range, end_of_range)

        samples = []
        samples = gen.sample_without_replacement(samples_len)


    except Exception as e:
        print(e.getMessage())
        DataGenerator.usage()


if __name__ == "__main__":
    main()
