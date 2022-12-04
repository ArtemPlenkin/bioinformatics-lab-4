import os
from metaflow import FlowSpec, step

class LinearFlow(FlowSpec):

    @step
    def start(self):
        os.system('fastqc SRR8533688.fastq.gz')
        os.system('bwa index ref_genome.fna')
        os.system('bwa mem ref_genome.fna SSRR8533688.fastq.gz > result.sam')
        os.system('samtools flagstat result.sam > final')
        os.system('python3 quality_check.py final')
        self.next(self.second)

    @step
    def second(self):
        print('Next step')
        self.next(self.end)

    @step
    def end(self):
       print('Finish')

if __name__ == '__main__':
    LinearFlow()