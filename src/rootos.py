import os
import yaml
import argparse

def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, str):
            path = os.path.join(base_path, item)
            os.makedirs(path, exist_ok=True)
        elif isinstance(item, dict):
            for k, v in item.items():
                path = os.path.join(base_path, k)
                os.makedirs(path, exist_ok=True)
                create_structure(path, v)

def main():
    parser = argparse.ArgumentParser(description="RootOS Directory Generator")
    parser.add_argument("--path", default=os.getcwd(), help="Target path")
    parser.add_argument("--config", default="config/rootos.yaml", help="Config file")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)

    root_dir = os.path.join(args.path, cfg["root"])
    os.makedirs(root_dir, exist_ok=True)

    create_structure(root_dir, cfg["structure"])
    print(f"[RootOS] Initialized at: {root_dir}")

if __name__ == "__main__":
    main()
