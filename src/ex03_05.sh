#! /bin/bash
echo "프로그램을 시작합니다."
read option
my_function() {
    echo '함수 안으로 들어왔습니다'
    result=`ls`
    echo $result
}
my_function