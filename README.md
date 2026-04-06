# FinReflectKG: Temporal GraphRAG with Soft Logic

**KR 2026 Submission - HONEST ARCHITECTURE**

A multi-hop financial QA system using temporal knowledge graphs and hinge-loss soft logic constraints.

## Quick Start

```bash
# Install dependencies
pip install rustworkx faiss-cpu sentence-transformers google-generativeai scipy numpy rich

# Run the notebook
jupyter notebook FinReflectKG_Complete_Pipeline.ipynb
```

## Architecture (Honest Claims Only)

```
Query → [FAISS Vector Search] → Anchor Nodes
                                      ↓
       [RustworkX Path Enumeration] ← with limits (100 max)
                                      ↓
       [Hinge-Loss PSL Solver] ← L-BFGS-B optimizer
                                      ↓
       [Prompt Grounder] → Gemini 2.5 Flash Lite → Answer
```

## Components

| Component | What It Does | What It's NOT |
|-----------|--------------|---------------|
| **Petagraph** | Temporal KG with edge decay | - |
| **HingeLossPSLSolver** | L-BFGS-B on hinge loss | NOT ADMM |
| **PromptGrounder** | Evidence-constrained prompts | NOT Logit Bias |

## Mathematical Foundation

### Temporal Decay
$$W(t) = W_0 \cdot e^{-\lambda (t_{ref} - t_{entry})}$$

### Hinge Loss Objective
$$\min_I \sum_r \lambda_r \cdot [\max(0, I(Body) - I(Head))]^2$$

### Path Interpretation (Geometric Mean)
$$I(Body) = \exp\left(\frac{1}{n} \sum_{e \in Path} \log W(e)\right)$$

## Data

- **Entities:** 1,030,398 nodes
- **Relations:** 4,920,816 edges  
- **Relation Schema:** 13,222 unique relation types
- **Temporal Range:** 2020-2024 financial filings

## Configuration

```python
REFERENCE_DATE = 20241231     # Latest data point
DECAY_LAMBDA = 0.001          # Temporal decay rate
PATH_LIMIT = 50               # Max paths to PSL solver
MAX_TOTAL_PATHS = 100         # Global path limit
PSL_MAX_ITER = 100            # L-BFGS-B iterations
```

## What We DON'T Claim

| Removed | Why |
|---------|-----|
| ~~ADMM~~ | We use L-BFGS-B, not ADMM |
| ~~HL-MRF~~ | No factor graph structure |
| ~~RLVR~~ | No reinforcement learning |
| ~~Logit Bias~~ | Groq API doesn't support it |
| ~~Virtual LoRA~~ | We don't modify model weights |

## Files

```
CAL/
├── FinReflectKG_Complete_Pipeline.ipynb  # Main notebook
├── README.md                              # This file
├── data/
│   ├── entity2id.txt                     # Node names
│   ├── relation2id.txt                   # Edge relations
│   └── train.txt                         # Graph triples
├── outputs/
│   ├── node_embeddings.faiss             # FAISS index
│   ├── node_mapping.json                 # Name → ID
│   └── knowledge_graph.pkl               # Petagraph
└── docs/
    ├── ARCHITECTURE.md                   # System design
    └── CRITIQUE.md                       # Code review
```

## Performance

With path limits:
- Vector Search: ~50ms
- Pathfinding: ~500ms (bounded)
- PSL Solve: ~100ms
- LLM Call: ~1-2s
- **Total: ~2-3s per query**

## Citation

```bibtex
@inproceedings{finreflectkg2026,
  title={FinReflectKG: Temporal GraphRAG with Soft Logic Constraints},
  booktitle={Proceedings of KR 2026},
  year={2026},
  note={Honest architecture: L-BFGS-B, not ADMM}
}
```

## License

Research use only (KR 2026 submission).
