import argparse
from db.database import init_db
from app.queries.run_qeries import run_queries
from app.db_manager import modify_database


def main():
    parser = argparse.ArgumentParser(description="Choose an operation mode.")
    parser.add_argument(
        "--mode",
        required=True,
        help="Operation mode",
        choices=["ExecuteQueries", "ModifyDatabase"],
    )
    args = parser.parse_args()

    init_db()

    if args.mode == "ExecuteQueries":
        run_queries()
    elif args.mode == "ModifyDatabase":
        modify_database()


if __name__ == "__main__":
    main()
