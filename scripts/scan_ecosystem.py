#!/usr/bin/env python3
import os
import json
import subprocess
import sys
from collections import defaultdict

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.live import Live

def scan_repos():
    console = Console()
    parent_dir = os.path.dirname(os.getcwd())
    repos = [
        "Causm", "Lila", "argus", "iris", "nimue-prism", "nimue-zig", 
        "nimue", "ocular", "mirage-fs", "astraea", "Sigilus", 
        "Project-Aether", "vizx", "Velhara", "chronos-db", "vortex-js", "rusty-palm"
    ]
    
    total_loc = 0
    language_stats = defaultdict(lambda: {"code_lines": 0, "files_count": 0})
    repo_data = {}
    
    repo_table = Table(title="Repository Statistics", show_header=True, header_style="bold cyan")
    repo_table.add_column("Repository", style="cyan")
    repo_table.add_column("Lines of Code", justify="right", style="green")
    repo_table.add_column("Primary Lang", style="yellow")
    
    with Live(repo_table, console=console, refresh_per_second=10):
        for repo in repos:
            repo_path = os.path.join(parent_dir, repo)
            if not os.path.exists(repo_path):
                repo_path = os.path.join(parent_dir, repo.lower())
                if not os.path.exists(repo_path):
                    continue
            try:
                # Run gstats with --json
                result = subprocess.run(
                    ["./scripts/gstats", repo_path, "--json"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                data = json.loads(result.stdout)
                
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
                
                repo_table.add_row(repo, f"{adjusted_repo_loc:n}", primary_lang)
                
            except Exception as e:
                console.print(f"[bold red]Error scanning {repo}:[/bold red] {e}")

    total_panel = Panel(
        Text(f"{total_loc:n}", justify="center", style="bold green on black"), 
        title="[bold]TOTAL LINES OF CODE[/bold]", 
        expand=False
    )
    console.print()
    console.print(total_panel)
    console.print()
    
    lang_table = Table(title="Language Breakdown (Aggregated)", show_header=True, header_style="bold cyan")
    lang_table.add_column("Language", style="cyan")
    lang_table.add_column("Total Code Lines", justify="right", style="green")
    lang_table.add_column("Files Count", justify="right", style="yellow")
    
    sorted_langs = sorted(language_stats.items(), key=lambda x: x[1]["code_lines"], reverse=True)
    languages_out = []
    
    for lang, stats in sorted_langs:
        lang_table.add_row(lang, f"{stats['code_lines']:n}", f"{stats['files_count']:n}")
        languages_out.append({
            "name": lang,
            "loc": stats["code_lines"],
            "files": stats["files_count"]
        })

    console.print(lang_table)

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
        
    console.print(f"\n[bold green][+][/bold green] Saved statistics to [bold cyan]{out_path}[/bold cyan]")

if __name__ == "__main__":
    scan_repos()
