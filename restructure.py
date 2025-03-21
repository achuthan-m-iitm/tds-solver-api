# import os
# import shutil

# # Define the new folder structure
# folders = [
#     "routers",
#     "services/function_solvers",
#     "utils",
#     "data",
#     "temp",
# ]

# files_to_move = {
#     "generate_tds_solver.py": "services/dispatcher.py",
#     "tds_ga_questions.json": "data/tds_ga_questions.json",
#     "uploaded.csv": "data/uploaded.csv",
#     "temp.zip": "temp/temp.zip",
# }

# folders_to_move = {
#     "unzipped": "temp/unzipped",
#     "api": "services",  # Assuming this has logic that belongs in services
# }

# files_to_delete = [
#     "vercel.json",
# ]

# def make_dirs():
#     for folder in folders:
#         os.makedirs(folder, exist_ok=True)

# def move_files():
#     for src, dest in files_to_move.items():
#         if os.path.exists(src):
#             shutil.move(src, dest)
#             print(f"Moved {src} → {dest}")
#         else:
#             print(f"Skipped missing file: {src}")

# def move_folders():
#     for src, dest in folders_to_move.items():
#         if os.path.exists(src):
#             shutil.move(src, dest)
#             print(f"Moved folder {src} → {dest}")
#         else:
#             print(f"Skipped missing folder: {src}")

# def delete_files():
#     for f in files_to_delete:
#         if os.path.exists(f):
#             os.remove(f)
#             print(f"Deleted {f}")
#         else:
#             print(f"Skipped missing file: {f}")

# def main():
#     print("🔧 Restructuring TDS Project 2 folders...")
#     make_dirs()
#     move_files()
#     move_folders()
#     delete_files()
#     print("\n✅ Restructure complete! Please review the changes.")

# if __name__ == "__main__":
#     main()
