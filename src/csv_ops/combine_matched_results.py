import pandas as pd

# Load Turkish and English similarity results
df_tr = pd.read_csv("../../data/outputs/combined_results_tr.csv")
df_en = pd.read_csv("../../data/outputs/combined_results_en.csv")

# Merge on 'file1' and 'file2' to match document pairs
df_combined = pd.merge(
    df_tr, df_en, on=["file1", "file2"], how="inner", suffixes=("_tr", "_en")
)

# Save the merged results
df_combined.to_csv(
    "../../data/outputs/final_combined_results.csv", index=False, encoding="utf-8"
)

print("Merged file saved as 'final_combined_results.csv'")
