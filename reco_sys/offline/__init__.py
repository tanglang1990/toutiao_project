from pyspark import SparkConf
from pyspark.sql import SparkSession

#import os
# os.environ['PYTHONUNBUFFERED'] = '1'
# os.environ['JAVA_HOME'] = '/root/bigdata/jdk'
# os.environ['SPARK_HOME'] = '/root/bigdata/spark'
# os.environ['HADOOP_HOME'] = '/root/bigdata/hadoop'
# os.environ['PYSPARK_PYTHON'] = '/root/anaconda3/envs/reco_sys/bin/python'
# os.environ['PYSPARK_DRIVER_PYTHON'] = '/root/anaconda3/envs/reco_sys/bin/python'


class SparkSessionBase(object):
    SPARK_APP_NAME = None
    SPARK_URL = "yarn"

    SPARK_EXECUTOR_MEMORY = "2g"
    SPARK_EXECUTOR_CORES = 2
    SPARK_EXECUTOR_INSTANCES = 2

    ENABLE_HIVE_SUPPORT = False

    def _create_spark_session(self):
        """给spark程序创建初始化spark session"""
        # 1、创建配置
        conf = SparkConf()

        config = (
            ("spark.app.name", self.SPARK_APP_NAME),  # 设置启动的spark的app名称，没有提供，将随机产生一个名称
            ("spark.executor.memory", self.SPARK_EXECUTOR_MEMORY),  # 设置该app启动时占用的内存用量，默认2g
            ("spark.master", self.SPARK_URL),  # spark master的地址
            ("spark.executor.cores", self.SPARK_EXECUTOR_CORES),  # 设置spark executor使用的CPU核心数，默认是1核心
            ("spark.executor.instances", self.SPARK_EXECUTOR_INSTANCES)
        )

        conf.setAll(config)

        # 2、读取配置初始化
        # 如果过开启HIVE信息
        if self.ENABLE_HIVE_SUPPORT:
            return SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
        else:
            return SparkSession.builder.config(conf=conf).getOrCreate()
