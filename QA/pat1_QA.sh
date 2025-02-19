#!/bin/sh
../../start.sh 
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/access.log /logstat/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \

-file ../../../mapreduce-test-python/logstat/mapper.py -mapper ../../../mapreduce-test-python/logstat/mapper.py \

-file ../../mapreduce-test-python/logstat/reducer.py -reducer ../../mapreduce-test-python/logstat/reducer.py \
-input /logstat/input/* -output /logstat/output/
/usr/local/hadoop/bin/hdfs dfs -cat /logstat/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat/output/
../../stop.sh
