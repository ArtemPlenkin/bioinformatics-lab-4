fastqc SRR8533688.fastq.gz			
bwa index ref_genome.fna
bwa mem ref_genome.fna SRR8533688.fastq.gz > result.sam						
samtools flagstat result.sam > final
python3 quality_check.py final
