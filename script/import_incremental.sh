#!/bin/bash

## user_profile
#sqoop import \
#        --connect jdbc:mysql://192.168.19.137/toutiao \
#        --username root \
#        --password password \
#        --table user_profile \
#        --m 4 \
#        --target-dir /user/hive/warehouse/toutiao.db/user_profile \
#        --incremental lastmodified \
#        --check-column update_time \
#        --merge-key user_id \
#        --last-value "2018-01-01 00:00:00"
sqoop import --connect jdbc:mysql://192.168.19.137/toutiao  --username root  --password password  --table user_profile  --m 4  --target-dir /user/hive/warehouse/toutiao.db/user_profile  --incremental lastmodified  --check-column update_time  --merge-key user_id  --last-value "2018-01-01 00:00:00"
