#!/bin/bash


while read sample;do
    echo $sample
    ./cas-offinder ./Input/${sample}.txt G ./Output/FirstResult/${sample}_result.txt > ./Log/${sample}_log.txt 2>&1 &
done < SampleList.txt
