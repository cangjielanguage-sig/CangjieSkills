# Knowledge Graph Template

Build your own knowledge graph to guide Cangjie App development.

## Quick Start

```bash
# 1. Add your docs/code
cp your_docs/*.md docs/
cp your_code/*.cj docs/

# 2. Build graph
python cli.py build docs/ --output data/graph.json

# 3. Query
python cli.py search "your term" --limit 5
python cli.py god-nodes --top-n 10

# 4. Export report
python cli.py export --graph data/graph.json --format report
```

## Dependencies

```bash
pip install tree-sitter-python networkx leidenalg
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `build docs/` | Build graph |
| `search "term"` | Search nodes |
| `traverse "term"` | Discover connections |
| `path "A" "B"` | Find path |
| `god-nodes` | Core concepts |
| `surprises` | Surprising connections |
| `export --format report` | Export analysis |

## Documentation

See `SKILL.md` for:
- Layered graph structure (L1/L2/L3)
- Python API for agents
- Integration with Cangjie App development