to_move = [
    "2023/5_may/3_dask_tutorial",
    "2023/12_december/3_intro_dbt",
    "2024/1_january/2_mongodb",
    "2024/1_january/1_databricks",
    "2024/1_january/3_snowflake",
    "2024/1_january/4_intro_to_nannyml",
    "2024/2_february/2_xgen",
    "2024/2_february/1_langsmith",
    "2024/2_february/4_dataclasses",
    "2024/3_march/1_rl",
    "2024/3_march/3_snowflake_time_travel",
    "2024/3_march/2_postgresml",
    "2024/4_april/2_chatgpt_wrappers",
    "2024/4_april/3_snowflake_snowpark",
    "2024/4_april/1_context_managers",
    "2024/5_may/2_misrtal_x22b",
    "2024/5_may/3_vertex_ai",
    "2024/5_may/1_dijkstra",
    "2024/5_may/4_aws_sagemaker",
    "2024/6_june/1_clone_branch",
    "2024/6_june/3_dvc_datacamp",
    "2024/6_june/4_gradio_tutorial",
    "2024/7_july/1_pytorch_lightning",
    "2024/7_july/4_sgd",
    "2024/7_july/5_vision_projects",
    "2024/7_july/6_grafana",
    "2024/7_july/7_langchain_agents",
    "2024/8_august/1_adam_optimizer",
    "2024/8_august/2_rag_langchain",
    "2024/8_august/4_sarsa",
    "2024/9_september/1_structured_outputs_openai",
    "2024/9_september/2_rmsprop",
    "2024/9_september/3_neo4j_python",
    "2024/9_september/4_llm_ui_streamlit",
    "2024/10_october/1_llm_ui_streamlit",
    "2024/10_october/2_java_interview_questions",
    "2024/10_october/3_python_vs_java",
    "2024/10_october/4_torch_rl",
    "2024/11_november/1_oop_java",
    "2024/11_november/2_python_poetry",
    "2024/11_november/3_learning_pytorch",
    "2024/11_november/4_uv_python",
]

# Move these directories to ~/datacamp_articles
# from pathlib import Path
# import shutil

# target_base = Path.home() / "datacamp_articles"

# # Create target base directory if it doesn't exist
# target_base.mkdir(parents=True, exist_ok=True)

# for path in to_move:
#     # Create full source and target paths
#     source = Path(path)
#     target = target_base / path

#     # Create parent directories
#     target.parent.mkdir(parents=True, exist_ok=True)

#     # Move directory
#     if source.exists():
#         shutil.move(str(source), str(target))
#         print(f"Moved {source} to {target}")
#     else:
#         print(f"Source {source} does not exist")

# Remove directories from git history using git filter-branch
import subprocess

for path in to_move:
    try:
        # Use git filter-branch to remove directory from history
        cmd = [
            "git",
            "filter-branch",
            "--force",
            "--index-filter",
            f'git rm -rf --cached --ignore-unmatch "{path}"',
            "--prune-empty",
            "--tag-name-filter",
            "cat",
            "--",
            "--all",
        ]
        subprocess.run(cmd, check=True)
        print(f"Removed {path} from git history")
    except subprocess.CalledProcessError as e:
        print(f"Error removing {path} from git history: {e}")

# Force garbage collection and remove old refs
cleanup_commands = [
    [
        "git",
        "for-each-ref",
        "--format='%(refname)'",
        "refs/original/",
        "--exec=git",
        "update-ref",
        "-d",
        "{}",
    ],
    ["git", "reflog", "expire", "--expire=now", "--all"],
    ["git", "gc", "--prune=now", "--aggressive"],
]

for cmd in cleanup_commands:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during cleanup: {e}")

print("Git history cleanup completed")
