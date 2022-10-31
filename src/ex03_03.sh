#! /bin/bash
read weight height
a=`expr $height \* $height`
b=`echo "$a/10000" | bc -l`
# if [`expr $weight  \ expr`$height * $height``]
lowerBound=18.5
upperBound=23
bmi=`echo "$weight/$b" | bc -l`
if [[`echo "$bmi < $lowerBound"|bc -l` -eq 1]]

then
    echo '저체중입니다'

elif [[$lowerBound -le ${bmi}] && [${bmi} -le $upperBound]]
then 
    echo '정상입니다.'
else
    echo "과체중입니다"
fi