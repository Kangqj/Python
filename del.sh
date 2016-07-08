#! /bin/bash
historyDir=~/test/
today=$(date +%Y-%m-%d)
echo "---------today is $today-----------"
today1=`date -j -f %Y-%m-%d $today +%s`
#echo "today1=$today1"

#求一周前的时间
tt=$(date -v -7d +%Y-%m-%d)
echo "next is to delete release before $tt"
tt1=`date -j -f %Y-%m-%d $tt +%s`   #linux上可以这样`date -d $tt +%s`  #小于此数值的文件夹删掉
#echo $tt1 
for file in ${historyDir}*
do 
    if test -d $file
    then
    name=`basename $file`
    echo $name
    curr=`date -j -f %Y-%m-%d $name +%s`
    if [ $curr -le $tt1 ]
        then
            echo " delete $name"
            rm -rf ${historyDir}${name}
    fi      
    fi
done
echo "--------------end---------------"