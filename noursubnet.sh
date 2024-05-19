#!/bin/bash

for i in {1..254} ; 
        for r in {1..254} ;
                for n in {1..254};
                        for m in {1.254};
                            do (proxychains4 ping -c 1 $i.$r.$n.$m > /dev/null 2>&1 | grep "bytes from" &) ;done

