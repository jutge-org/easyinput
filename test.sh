#!/bin/bash


cd test

for d in *.tst ; do

    cd $d
    cp -r ../../jutge .

    for t in *.inp ; do

        echo $d/$t

        t=`basename $t .inp`
        python test.py <$t.inp >$t.out
        diff $t.out $t.cor

    done

    cd ..

done
