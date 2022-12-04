# Part 1 

1. [Референсный геном e.coli](/input/ref_genome.fna)
2. [Ссылка на загруженные прочтения из NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/?term=SRR8533688)
3. [Bash скрипт с реализованным алгоритмом](/input/bash.sh)
4. [Результат команды samtools flagstat](/generated/final)

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

# Part 3

1. [Код пайплана](/input/main.py)
2. Все сгенерированные файлы в ходе работы пайплайна [здесь](/generated)
3. По итогу в консоль выводится результат "OK" или "Not OK"
4. [Лог из консоли](/metaflow_final.log)
5. Визуализация пайплайна автоматически, через введение команды *python3 main.py card get start mycard.html*, а также подставив @card перед основным алгоритмом. Тем самым сгенерируется файл [mycard.html](/generated/mycard.html)
![image](https://user-images.githubusercontent.com/61593324/205484488-eb8d970d-102a-4dff-a87d-97d34f663c16.png)

Здесь каждый блок схемы отвечает за выполнение команды [скрипта](/input/bash.sh)

Полученная схема визуализации отличается от блок-схемы алгоритма из задания:
1. входные файлы на схеме не помечаются
2. у блока start (fastqc) нет ответвления для создания отчета, хотя fastqc создает отчет
3. условный оператор на проверку процента и последующее ветвление отображается как один блок внутри, которого и происходит проверка
