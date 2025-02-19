#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/access.log /lab1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /lab1/input/* -output /lab1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /lab1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output/
