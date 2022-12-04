# Part 1 

1. [Референсный геном e.coli](/Part1/ref_genome.fna)
2. [Ссылка на загруженные прочтения из NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/?term=SRR8533688)
3. [Bash скрипт с реализованным алгоритмом](/bash.sh)
4. [Результат команды samtools flagstat](/final.txt)

# Part 2

Инструкция по развертыванию и установке фреймворка:
1) Проверить, что установлен Python 3 или более поздняя версия.  
```
python --version
```
2) Ввести команду в терминал
```
pip install metaflow
```
3) Теперь можно запустить классический Hello world, используя следующие команды:  
```
metaflow tutorials pull
cd metaflow-tutorials
python3 00-helloworld/helloworld.py show
python3 00-helloworld/helloworld.py run
```
Как результат работы получаем:  
1. [Папка metaflow](/.metaflow)
2. [Логи](/metaflow.log)
