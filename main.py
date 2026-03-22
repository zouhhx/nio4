import pandas as pd
import os
import glob
import logging
import matplotlib.pyplot as plt

output_dir = "test_results"
os.makedirs(output_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=os.path.join(output_dir, 'analysis.log'),
    filemode='w'
)

def analyze(file):
 try:
    df = pd.read_csv(file)
 except FileNotFoundError:
    logging.error(f"错误：文件 {file} 不存在")
    return None, None

 success = (df["result"]=="success").sum()
 fail = (df["result"]=="fail").sum()

 return success, fail

if __name__ == "__main__":
 
    csv_files = glob.glob("*.csv")
    
    total_s, total_f = 0, 0
    
    logging.info(f"Detected {len(csv_files)} test files.")
    for f in csv_files:
        s, f_count = analyze(f)
        total_s += s
        total_f += f_count

    total_tests = total_s + total_f
    total_rate = total_s / total_tests if total_tests > 0 else 0

    report_path = os.path.join(output_dir, 'summary_report.txt')
    with open(report_path, "w") as report:
        report.write(f"Total Files Processed: {len(csv_files)}\n")
        report.write(f"Total Success: {total_s}\n")
        report.write(f"Total Fail: {total_f}\n")
        report.write(f"Total Rate: {total_rate*100:.2f}%\n")

    plt.figure(figsize=(6, 6))
    plt.pie([total_s, total_f], labels=['Success', 'Fail'], colors=['#4CAF50', '#F44336'], autopct='%1.1f%%')
    plt.title(f'Total Parking Performance (n={total_tests})')
    plt.savefig(os.path.join(output_dir, 'summary.png'))
    
    print(f"Done! Results are in the '{output_dir}' folder.")
    logging.info("Automation task completed successfully.")