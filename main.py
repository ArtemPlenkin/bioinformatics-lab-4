import os
from metaflow import FlowSpec, step

class LinearFlow(FlowSpec):

    @step
    def first(self):
        os.system('fastqc SRR8533688.fastq.gz')
        self.next(self.second)

    @step
    def second(self):
        os.system('bwa index ref_genome.fna')
        self.next(self.third)

    @step
    def third(self):
        os.system('bwa mem ref_genome.fna SSRR8533688.fastq.gz > result.sam')
        self.next(self.forth)

    @step
    def third(self):
        os.system('samtools flagstat result.sam > final')
        self.next(self.fifth)

    @step
    def fifth(self):
        os.system('python3 quality_check.py final')

if __name__ == '__main__':
    LinearFlow()