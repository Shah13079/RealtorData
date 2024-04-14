# import os
# import csv

# folder_path = "scrape_06_30_2023"  # Replace with the actual folder path

# # Iterate over files in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith(".csv"):
#         file_path = os.path.join(folder_path, filename)
#         with open(file_path, "r",  encoding="utf-8") as file:
#             csv_reader = csv.reader(file)
#             row_count = sum(1 for row in csv_reader)
#             print(f"File: {filename}, Rows: {row_count}")
