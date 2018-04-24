#!/bin/bash
for value in {1..10}
do
n=$((RANDOM%100000+100000))
docker run -d -m="50mb" --memory-swap="4096mb" number-sort python ./randomNumberSort.py $RANDOM $n
done

