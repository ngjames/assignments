#!/bin/bash

cut -f1,4 $1 | grep "/products/" | sort -k1 | sort -k3 | uniq