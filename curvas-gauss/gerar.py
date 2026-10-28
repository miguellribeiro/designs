"""Gera as três curvas de Gauss em alto contraste para projetor."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm, skewnorm
from pathlib import Path

CURVAS = [
    ("curva-gauss-padrao", "Curva de Gauss padrão", "#0047FF", lambda x: norm.pdf(x)),
    ("curva-gauss-acentuada-crescente", "Curva acentuada crescente", "#E6002E",
     lambda x: skewnorm.pdf(x, 6, loc=-1.6, scale=2.2)),
    ("curva-gauss-acentuada-decrescente", "Curva acentuada decrescente", "#FF6A00",
     lambda x: skewnorm.pdf(x, -6, loc=1.6, scale=2.2)),
]

script_dir = Path(__file__).parent
output_dir = script_dir / "imagens"
output_dir.mkdir(exist_ok=True)

x = np.linspace(-4, 4, 1200)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.weight": "bold"})
for nome, titulo, cor, f in CURVAS:
    y = f(x)
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.patch.set_facecolor("white"); ax.set_facecolor("white")
    ax.grid(True, color="#A6A6A6", linewidth=2.5, linestyle="--", alpha=1)
    ax.fill_between(x, y, color=cor, alpha=.45, zorder=2)
    ax.plot(x, y, color=cor, linewidth=13, solid_capstyle="round", zorder=3)
    xp = x[np.argmax(y)]
    ax.vlines(xp, 0, y.max(), colors="#111111", linewidth=6, linestyles="dashed", zorder=4)
    ax.set_xlim(-4, 4); ax.set_ylim(0, 0.5)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(7); ax.spines[s].set_color("#111111")
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=26)
    ax.plot(-4, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=26)
    ax.tick_params(width=6, length=16, labelsize=22, colors="#111111")
    ax.set_xlabel("x", fontsize=34, fontweight="bold", color="#111111", labelpad=10)
    ax.set_ylabel("y", fontsize=34, fontweight="bold", color="#111111", rotation=0, labelpad=30)
    ax.set_title(titulo, fontsize=30, fontweight="bold", color="#111111", pad=24)
    fig.tight_layout()
    fig.savefig(output_dir / f"{nome}.png", facecolor="white")
    plt.close(fig)
print("ok")
