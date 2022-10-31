#! /bin/bash
read file
state=0
for var in `ls`
do
    if [ $var -eq &state]
    then 
        state=1
    fi

done
if [ &state -eq 1]
then 
    echo "찾으시는 파일이 안에 있습니다. "
else
    echo ''