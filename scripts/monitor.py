from pathlib import Path
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ROOT / "artifacts"

def create_drift_report():
    reference = pd.read_csv(ARTIFACTS / "reference_data.csv")
    current = pd.read_csv(ARTIFACTS / "current_data.csv")

    # Demonstration only: in deployment, replace current_data.csv with
    # recent production input data collected with appropriate permission.
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)
    output = ARTIFACTS / "data_drift_report.html"
    report.save_html(str(output))
    print(f"Evidently report saved to: {output}")

if __name__ == "__main__":
    create_drift_report()
