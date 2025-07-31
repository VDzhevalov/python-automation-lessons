from datetime import datetime
import re

def analyze_heartbeat_log(input_file: str, output_file: str, key: str):
    time_pattern = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2})")
    filtered_lines = []


    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if key in line:
                match = time_pattern.search(line)
                if match:
                    timestamp = datetime.strptime(match.group(1), "%H:%M:%S")
                    filtered_lines.append((timestamp, line.strip()))


    with open(output_file, "w", encoding="utf-8") as log:
        for i in range(1, len(filtered_lines)):
            prev_time, _ = filtered_lines[i - 1]
            curr_time, _ = filtered_lines[i]


            diff = (prev_time - curr_time).total_seconds()
            if diff < 0:
                diff += 86400

            if 31 < diff < 33:
                log.write(f"WARNING: Delay {diff:.0f} sec at {curr_time.strftime('%H:%M:%S')}\n")
            elif diff >= 33:
                log.write(f"ERROR: Delay {diff:.0f} sec at {curr_time.strftime('%H:%M:%S')}\n")

#Додав як txt бо log в gitignore
if __name__ == "__main__":
    analyze_heartbeat_log(
        input_file="hblog.txt",
        output_file="hb_test.txt",
        key="Key TSTFEED0300|7E3E|0400"
    )