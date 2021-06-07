#!/usr/bin/env bash

if [[ -n $1 ]]
then
    arg="$1"
    if [[ "$arg" = "bad" ]]
    then
        echo "Bad argument"
        exit 1
    fi
else
    arg="world"
fi

echo "Hello $arg"
echo "Goodbye"

