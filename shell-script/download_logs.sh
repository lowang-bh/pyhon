#!/usr/bin/env bash

if [[ $# -ne 2 ]];then
    echo $"Usage: $0 {year} {month}; example: $0 2019 01"
    exit 1
fi

case "$2" in
        01)
            for i in {01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
            do
                bash get_log_from_hadoop.sh social-network-yrd $1$2$i
            done
            ;;
        02)
            for i in {01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28};
            do
                bash get_log_from_hadoop.sh social-network-yrd  $1$2$i
            done
            ;;
         
        03)
            for i in {01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
            do
                bash get_log_from_hadoop.sh social-network-yrd  $1$2$i
            done
            ;;
        04)
            for i in {01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30};
            do
                bash get_log_from_hadoop.sh social-network-yrd  $1$2$i
            done
            ;;
        05)
            for i in {01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
            do
                bash get_log_from_hadoop.sh social-network-yrd  $1$2$i
            done
            ;;
        06)
            for i in {01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30};
            do
                bash get_log_from_hadoop.sh social-network-yrd  $1$2$i
            done
            ;;                                    
         
        *)
            echo $"Usage: $0 {year} {month}; example: $0 2019 01"
            exit 1
 esac
