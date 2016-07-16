#!/bin/bash


cd test
rm -rf jutge
cp -r ../jutge .
python sum.py <sum-test-1.inp >sum-test-1.out ; diff sum-test-1.out sum-test-1.cor
