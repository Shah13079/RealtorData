# import os

# def find_missing_state_files(folder_path):
#     state_files = set()
#     missing_states = set()

#     # Get a set of expected state abbreviations
#     expected_states = set(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
#                            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
#                            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
#                            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
#                            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'])

#     # Collect the existing state files in the folder
#     for filename in os.listdir(folder_path):
#         if filename.endswith('.csv'):
#             state = filename[:2].upper()
#             state_files.add(state)

#     # Find missing state files
#     missing_states = expected_states - state_files

#     return missing_states

# # Specify the folder path containing the state files
# folder_path = 'scrape_06_30_2023'  # Replace with the actual folder path

# # Call the function to find missing state files
# missing_files = find_missing_state_files(folder_path)

# # Print the missing state files
# print("Missing state files:")
# for state in missing_files:
#     print(state + '.csv')
