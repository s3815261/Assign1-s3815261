import random
import time
import sys


class DataGenerator:
    # Program name.
    prog_name = "DataGenerator"

    def __init__(self, start_of_range, end_of_range, samples_len, sample_data, operation, output):
        # Start of integer range to generate values from.
        self.start_of_range = start_of_range
        # End of integer range to generate values from.
        self.end_of_range = end_of_range
        # Random generator to use.
        random.seed(time.time())
        # Sample size
        self.samples_len = samples_len
        # Where the data is being samples from --> word frequency txt
        self.sampleData = sample_data
        # Operation to test / analyse
        self.operation = operation
        # Output of file sample
        self.output = output

    def make_sample(self, samples):
        """
        Take the samples and run them againest our sampledata and return a file that contains words
        where they are samples from our data samples
        """
        data = open(self.sampleData, "r")
        file_output = open(self.output, "w")
        for pos, line_num in enumerate(data):
            if pos in samples:
                if self.operation == "W":
                    # Just the word frequency (require frequency!)
                    file_output.write(line_num)
                elif self.operation == "A":
                    # For ADD (require frequency & operation!)
                    file_output.write(self.operation + " " + line_num)
                else:
                    # For SEARCH, AUTO COMPLETE & DELETE (don't require frequency!)
                    word = str.split(line_num)
                    file_output.write(self.operation + " " + word[0] + "\n")
        data.close()
        file_output.close()

    def sample_without_replacement(self):
        """
        Sample without replacement, using "Algorithm R" by Jeffrey Vitter, in paper "Random sampling without a reservoir".
        This algorithm has O(size of range) time complexity.

        @param samples_len Number of samples to generate.
        @throws IllegalArgumentException When samples_len is greater than the valid integer range.
        """
        population_size = self.end_of_range - self.start_of_range + 1

        if self.samples_len > population_size:
            raise ValueError("samples_len cannot be greater than population_size for sampling without replacement.");

        samples = []
        # fill it with initial values in the range
        for i in range(self.samples_len):
            samples.append(i + self.start_of_range)

        # replace
        for j in range(self.samples_len, population_size):
            t = random.randint(0, j + 1)
            if t < self.samples_len:
                samples[t] = j + self.start_of_range
        return samples

    @staticmethod
    def usage():
        """
        Error Message
        """
        print(
            DataGenerator.prog_name + ": <start of range to sample from> <end of range to sample from> <number of "
                                      "values to sample> <sample file> <operation - A,S,D,AC,W > <output>")
        exit(1)


def main():
    # check correct number of command line arguments
    args = sys.argv[1:]
    if len(args) != 6:
        DataGenerator.usage()

    try:
        # integer range
        start_of_range = int(args[0])
        end_of_range = int(args[1])

        # number of values to sample
        samples_len = int(args[2])

        # Get sampleData file
        sample_data = str(args[3])

        # What operation to test
        operation = str(args[4])

        # Name of output file
        output = str(args[5])

        # gen = DataGenerator(start_of_range, end_of_range)
        if operation != "A" and operation != "S" and operation != "D" and operation != "AC" and operation != "W":
            print("incorrect operation: A ADD, S SEARCH, D DELETE, AC AUTO COMPLETE, W JUST WORDS")
            DataGenerator.usage()

        samples = []
        # python3 datagen.py 1 100 20 data/sampleData.txt W add20.txt
        gen = DataGenerator(start_of_range, end_of_range, samples_len, sample_data, operation, output)
        samples = gen.sample_without_replacement()
        gen.make_sample(samples)
        print("SUCCESS! File will print shortly, depending on size may take a few mins... ")

    except Exception as e:
        print(e.getMessage())
        DataGenerator.usage()


if __name__ == "__main__":
    main()
