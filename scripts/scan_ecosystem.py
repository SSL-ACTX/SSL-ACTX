#!/usr/bin/env python3
import os
import json
import subprocess
import sys
from collections import defaultdict

def scan_repos():
    parent_dir = os.path.dirname(os.getcwd())
    repos = [
        "Causm", "Lila", "argus", "iris", "nimue-prism", "nimue-zig", 
        "nimue", "ocular", "mirage-fs", "astraea", "Sigilus", 
        "Project-Aether", "vizx"
    ]
    
    total_loc = 0
    language_stats = defaultdict(lambda: {"code_lines": 0, "files_count": 0})
    repo_data = {}
    
    print(f"{'Repository':<20} | {'Lines of Code':<15} | {'Primary Lang':<15}")
    print("-" * 55)
    
    for repo in repos:
        repo_path = os.path.join(parent_dir, repo)
        if not os.path.exists(repo_path):
            repo_path = os.path.join(parent_dir, repo.lower())
            if not os.path.exists(repo_path):
                continue
        try:
            # Run gstats with --json
            result = subprocess.run(
                [sys.executable, "scripts/gstats.py", repo_path, "--json"],
                capture_output=True,
                text=True,
                check=True
            )
            data = json.loads(result.stdout)
            
            repo_loc = data.get("summary", {}).get("code_lines", 0)
            
            repo_langs = data.get("languages", {})
            primary_lang = "Unknown"
            max_lang_loc = -1
            
            for lang, stats in repo_langs.items():
                if lang.upper() == "JSON":
                    continue # Ignore JSON in statistics
                
                l_code = stats.get("code_lines", 0)
                l_files = stats.get("files_count", 0)
                
                language_stats[lang]["code_lines"] += l_code
                language_stats[lang]["files_count"] += l_files
                
                if l_code > max_lang_loc:
                    max_lang_loc = l_code
                    primary_lang = lang
            
            # Recalculate repo loc excluding JSON
            adjusted_repo_loc = sum(stats.get("code_lines", 0) for lang, stats in repo_langs.items() if lang.upper() != "JSON")
            total_loc += adjusted_repo_loc
            
            repo_data[repo] = {
                "loc": adjusted_repo_loc,
                "primary_lang": primary_lang
            }
            
            print(f"{repo:<20} | {adjusted_repo_loc:<15n} | {primary_lang:<15}")
            
        except Exception as e:
            print(f"Error scanning {repo}: {e}")

    print("\n" + "=" * 55)
    print(f"{'TOTAL LINES OF CODE':<20} | {total_loc:<15n}")
    print("=" * 55)
    
    print("\nLanguage Breakdown (Aggregated):")
    print(f"{'Language':<20} | {'Total Code Lines':<15} | {'Files Count':<12}")
    print("-" * 55)
    
    sorted_langs = sorted(language_stats.items(), key=lambda x: x[1]["code_lines"], reverse=True)
    languages_out = []
    
    for lang, stats in sorted_langs:
        print(f"{lang:<20} | {stats['code_lines']:<15n} | {stats['files_count']:<12n}")
        languages_out.append({
            "name": lang,
            "loc": stats["code_lines"],
            "files": stats["files_count"]
        })

    # Save to generated/ecosystem_stats.json
    out_data = {
        "total_loc": total_loc,
        "repositories": repo_data,
        "languages": languages_out
    }
    
    os.makedirs("generated", exist_ok=True)
    out_path = os.path.join("generated", "ecosystem_stats.json")
    with open(out_path, "w") as f:
        json.dump(out_data, f, indent=2)
        
    print(f"\n[+] Saved statistics to {out_path}")

if __name__ == "__main__":
    scan_repos()