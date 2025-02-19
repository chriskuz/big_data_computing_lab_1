#!/bin/sh
read -p "Query start hour [XX] (00-17): " START
read -p "Query end hour [XX] (01-17): " END


echo "Running Hadoop job for time range: $START to $END..."

../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/access.log /lab1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer2.py \
-cmdenv START=$START \
-cmdenv END=$END
-input /lab1/input/* -output /lab1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /lab1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output/
../../../stop.sh
