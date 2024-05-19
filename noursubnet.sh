#!/bin/bash

for i in {1..254}; do
        for r in {1..254}; do
                for n in {1..254}; do
                        for m in {1.254};do
                                (proxychains4 ping -c 1 $i.$r.$n.$m > /dev/null 2>&1 | grep "bytes from" &) ;
done
done
done
done
