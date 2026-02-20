import re
import logging
from collections import defaultdict, Counter

# Configure logging so that messages are written
# both to file analysis_audit.log and the console.
# This helps track security warnings and system errors.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("analysis_audit.log"),
        logging.StreamHandler()
    ]
)


class LogAnalyzer:
    """
    This class reads an Apache-style server log file,
    extracts useful information, detects suspicious activity,
    and generates multiple reports based on the analysis.
    """

    def __init__(self, filename):
        # Store the name of the log file to analyze
        self.filename = filename

        # Regular expression pattern used to extract:
        # IP address, timestamp, HTTP method, URL,
        # status code, and response size from each log line.
        self.log_pattern = re.compile(
            r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+)'
        )

        # variables used to store traffic statistics
        self.total_requests = 0
        self.unique_ips = set()
        self.method_counts = Counter()
        self.url_counts = Counter()
        self.status_counts = Counter()
        self.errors = []

        # variables used to track potential security issues :)))
        self.failed_logins = defaultdict(int)
        self.security_incidents = []

    def parse_line(self, line):
        """
        Attempts to match a log line against the regex pattern.
        If successful, returns a dictionary of extracted values.
        If not, logs a warning and skips the line.
        """
        match = self.log_pattern.match(line)

        if not match:
            logging.warning("Skipping malformed log entry.")
            return None

        ip, timestamp, method, url, status, size = match.groups()

        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "url": url,
            "status": int(status),
            "size": int(size)
        }

    def check_security(self, entry):
        """
        Checks each log entry for common security threats:
        - Brute force login attempts
        - Forbidden resource access
        - Basic SQL injection keywords
        """

        # Detect brute force attempts (3 failed login attempts from the same IP)
        if entry["url"] == "/login" and entry["status"] == 401:
            self.failed_logins[entry["ip"]] += 1

            if self.failed_logins[entry["ip"]] == 3:
                message = f"Brute force attempt suspected from {entry['ip']}"
                self.security_incidents.append(message)
                logging.warning(message)

        # Detect attempts to access forbidden ports or entries
        if entry["status"] == 403:
            message = f"Forbidden access attempt: {entry['ip']} -> {entry['url']}"
            self.security_incidents.append(message)
            logging.warning(message)

        # Detect simple SQL injection patterns in URLs
        suspicious_words = ["select", "union", "drop", "--", ";"]
        url_lower = entry["url"].lower()

        for word in suspicious_words:
            if word in url_lower:
                message = f"Possible SQL injection attempt from {entry['ip']}"
                self.security_incidents.append(message)
                logging.warning(message)
                break

    def analyze_logs(self):
        """
        Opens the log file safely using 'with open'.
        Reads it line-by-line to handle large files efficiently.
        Updates statistics and performs security checks for each entry.
        """
        try:
            with open(self.filename, "r") as file:
                for line_number, line in enumerate(file, 1):

                    try:
                        entry = self.parse_line(line.strip())

                        if not entry:
                            continue

                        # Update traffic statistics
                        self.total_requests += 1
                        self.unique_ips.add(entry["ip"])
                        self.method_counts[entry["method"]] += 1
                        self.url_counts[entry["url"]] += 1
                        self.status_counts[entry["status"]] += 1

                        # Track HTTP errors,, status codes 400 and above..
                        if entry["status"] >= 400:
                            self.errors.append(entry)

                        # Perform security checks on each valid entry
                        self.check_security(entry)

                    except ValueError as e:
                        # Handles issues converting status or size to integers
                        logging.error(f"Line {line_number}: Data conversion error - {e}")

                    except Exception as e:
                        # Catches unexpected errors without stopping the program
                        logging.error(f"Line {line_number}: Unexpected error - {e}")

            logging.info("Log analysis completed successfully.")

        except FileNotFoundError:
            logging.critical("Log file not found.")
            print("Error: server.log does not exist.")

        except PermissionError:
            logging.critical("Permission denied reading log file.")
            print("Error: Cannot access log file.")

    def generate_summary(self):
        """
        Creates a summary report containing:
        - Total requests
        - Unique IP count
        - HTTP method distribution
        - Top 5 URLs
        - Status code distribution
        """
        with open("summary_report.txt", "w") as report:

            report.write("SERVER LOG SUMMARY\n")
            report.write("=" * 50 + "\n\n")

            report.write(f"Total Requests: {self.total_requests}\n")
            report.write(f"Unique IP Addresses: {len(self.unique_ips)}\n\n")

            report.write("HTTP Methods:\n")
            for method, count in self.method_counts.items():
                report.write(f"{method}: {count}\n")

            report.write("\nTop 5 URLs:\n")
            for url, count in self.url_counts.most_common(5):
                report.write(f"{url}: {count}\n")

            report.write("\nStatus Codes:\n")
            for status, count in sorted(self.status_counts.items()):
                report.write(f"{status}: {count}\n")

        logging.info("Summary report generated.")

    def generate_security_report(self):
        """
        Writes all detected security incidents to a separate file.
        This helps administrators review suspicious behaviour.
        """
        with open("security_report.txt", "w") as report:

            report.write("SECURITY INCIDENTS\n")
            report.write("=" * 50 + "\n\n")

            report.write(f"Total Incidents: {len(self.security_incidents)}\n\n")

            for incident in self.security_incidents:
                report.write(incident + "\n")

        logging.info("Security report generated.")

    def generate_error_report(self):
        """
        Writes all HTTP errors (status >= 400) to a report file
        including timestamp, IP address, method, URL, and status code.
        """
        with open("error_log.txt", "w") as report:

            report.write("HTTP ERRORS\n")
            report.write("=" * 50 + "\n\n")

            report.write(f"Total Errors: {len(self.errors)}\n\n")

            for error in self.errors:
                report.write(
                    f"[{error['timestamp']}] "
                    f"{error['ip']} - "
                    f"{error['method']} {error['url']} - "
                    f"Status {error['status']}\n"
                )

        logging.info("Error report generated.")


def main():
    """
    Main function that creates the analyzer object,
    runs the analysis, and generates all reports.
    """
    analyzer = LogAnalyzer("server.log")

    analyzer.analyze_logs()
    analyzer.generate_summary()
    analyzer.generate_security_report()
    analyzer.generate_error_report()

    print("\nAnalysis Complete!")
    print(f"Total Requests: {analyzer.total_requests}")
    print(f"Security Incidents: {len(analyzer.security_incidents)}")
    print(f"Errors Found: {len(analyzer.errors)}")


if __name__ == "__main__":
    main()
