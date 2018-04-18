#!/bin/bash
SCRIPT=$1

if [ $# -ne 1 ]; then
  echo "Usage: $0 <SCRIPT>"
  exit 0
fi

while :
do
  echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  echo "@ Execute python ${SCRIPT}"
  echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  python ${SCRIPT}
  echo ""
  echo "Sleeping 3s"
  sleep 3s
  echo ""
done

