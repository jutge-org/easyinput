#!/bin/bash


fail=0

cd test
for d in *.tst
do
    cd $d
    cp -r ../../jutge .
    for t in *.inp
    do
        t=`basename $t .inp`
        python test.py <$t.inp >$t.out
        cmp --silent $t.out $t.cor
        if [ $? -ne 0 ]
        then
            fail=1
            echo $d/$t fail
        else
            echo $d/$t ok
        fi
    done
    cd ..
done

exit $fail
