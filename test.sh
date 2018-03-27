#/bin/bash

echo "PING"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/"
printf '%.0s-' {1..20}; echo

echo "key"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/key"
printf '%.0s-' {1..20}; echo

echo "agent"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/agent"
printf '%.0s-' {1..20}; echo

echo "boot_time"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/boot_time"
printf '%.0s-' {1..20}; echo

echo "hostname"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/hostname"
printf '%.0s-' {1..20}; echo

echo "la"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/la"
printf '%.0s-' {1..20}; echo

echo "python"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/python"
printf '%.0s-' {1..20}; echo

echo "top5cpu"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/top5cpu"
printf '%.0s-' {1..20}; echo

echo "top5mem"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/top5mem"
printf '%.0s-' {1..20}; echo

echo "/cpu/info"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/cpu/info"
printf '%.0s-' {1..20}; echo

echo "/cpu/cpu_times"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/cpu/cpu_times"
printf '%.0s-' {1..20}; echo

echo "/cpu/cpu_percent"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/cpu/cpu_percent"
printf '%.0s-' {1..20}; echo

echo "/cpu/cpu_percent_total"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/cpu/cpu_percent_total"
printf '%.0s-' {1..20}; echo

echo "/cpu/cpu_stats"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/cpu/cpu_stats"
printf '%.0s-' {1..20}; echo

echo "/cpu/cpu_freq"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/cpu/cpu_freq"
printf '%.0s-' {1..20}; echo

echo "/disk/partitions"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/disk/partitions"
printf '%.0s-' {1..20}; echo

echo "/disk/disk_io_counters"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/disk/disk_io_counters"
printf '%.0s-' {1..20}; echo

echo "/disk/disk_rw"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/disk/disk_rw"
printf '%.0s-' {1..20}; echo

echo "/mem/virtual"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/mem/virtual"
printf '%.0s-' {1..20}; echo

echo "/mem/swap"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/mem/swap"
printf '%.0s-' {1..20}; echo

echo "/net/addr"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/net/addr"
printf '%.0s-' {1..20}; echo

echo "/net/counters"
curl -sS -X GET -H "api_key: 111" "http://127.0.0.1:9000/net/counters"
printf '%.0s-' {1..20}; echo