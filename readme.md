这是一个用于低速泊车测试的自动化分析工具。它可以一键读取多个 CSV 测试数据，计算泊车成功率，并自动生成日志和可视化饼图。



1\. 安装依赖：

pip install -r requirements.txt



2\. 运行分析：

python main.py



3\. 运行测试：

pytest



产出文件

程序运行后会自动生成 test\_results文件夹

包含：

summary\_report.txt：总成功率数据汇总

summary.png：可视化结果饼图

analysis.log：后台运行日志

