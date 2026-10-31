"""Saptarshi Das — Quantitative Analyst. One-page portfolio served by Streamlit."""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import quant

ROOT = Path(__file__).parent

NAME = "Saptarshi Das"
EMAIL = "saptarshi.das18@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/saptarshi-das-341495167"
CV_URL = "app/static/Saptarshi_Das_CV.pdf"  # served from ./static (enableStaticServing)

st.set_page_config(
    page_title=f"{NAME} · Quantitative Analyst",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_resource
def css() -> str:
    return f"<style>{(ROOT / 'style.css').read_text()}</style>"


@st.cache_resource
def hero_curve(w=420, h=130, n=90, seed=11) -> tuple[str, str]:
    """A deterministic upward-drifting equity curve for the hero SVG."""
    rng = np.random.default_rng(seed)
    y = np.cumsum(0.004 + 0.018 * rng.standard_normal(n))
    x = np.linspace(0, w, n)
    y = h - 8 - (y - y.min()) / (y.max() - y.min()) * (h - 20)
    line = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in zip(x, y))
    return line, f"{line} L{w},{h} L0,{h} Z"


def page(body: str) -> None:
    st.html(f'<div class="sd">{body}</div>')


st.html(css())

# --------------------------------------------------------------------- nav + hero
line, area = hero_curve()
ticker_items = ["Python", "Black-Scholes", "Binomial trees", "Implied volatility", "Greeks Δ Γ Θ ν ρ",
                "Event-driven backtesting", "NSE equities", "MCX commodities", "Delta hedging", "GCP BigQuery",
                "Mojo", "C++", "Machine learning", "Time-series forecasting", "Broker APIs", "Claude"]
ticker = "".join(f"<span>{t}</span>" for t in ticker_items) * 2

terminal = [
    ('<span class="p">❯</span> <span class="v">engine run --mode live --venue MCX</span>', 0.3),
    ('<span class="ok">✓</span> <span class="k">adapter</span>   <span class="v">backtest · paper · live</span>', 0.7),
    ('<span class="ok">✓</span> <span class="k">strategy</span>  <span class="v">vwap_reversion + bb_squeeze</span>', 1.0),
    ('<span class="ok">✓</span> <span class="k">greeks</span>    <span class="v">Δ Γ Θ ν ρ streaming</span>', 1.3),
    ('<span class="warn">●</span> <span class="k">risk</span>      <span class="v">daily loss limit armed</span>', 1.6),
]
term_lines = "".join(f'<div class="ln" style="animation-delay:{d}s">{t}</div>' for t, d in terminal)

page(f"""
<nav class="nav"><div class="wrap">
  <a class="logo" href="#top"><span class="logo-mark">SD</span>saptarshi.das</a>
  <div class="nav-links">
    <a href="#about">About</a><a href="#work">Work</a><a href="#journey">Journey</a>
    <a href="#skills">Toolkit</a><a href="#lab">Options Lab</a><a href="#contact">Contact</a>
  </div>
  <a class="nav-cta" href="{CV_URL}" download="Saptarshi_Das_CV.pdf">Résumé ↓</a>
</div></nav>

<header class="hero" id="top"><div class="wrap hero-grid">
  <div>
    <span class="status"><span class="dot"></span>Quantitative Analyst · Cloudcraftz AI</span>
    <h1>Turning market ideas into <em>live trading systems.</em></h1>
    <p class="sub">I'm <b>Saptarshi Das</b>. I research, backtest and deploy systematic strategies across
      <b>NSE equities</b> and <b>MCX commodities</b>, and build the options analytics and risk
      infrastructure that keeps them honest in production.</p>
    <div class="ctas">
      <a class="btn btn-solid" href="#work">See my work →</a>
      <a class="btn btn-line" href="{CV_URL}" download="Saptarshi_Das_CV.pdf">Download CV</a>
    </div>
    <div class="meta"><span>MBA · IIM Amritsar</span><span>Kolkata, India</span><span>2+ yrs in quant</span></div>
  </div>
  <div class="term">
    <div class="term-bar"><i></i><i></i><i></i><span>trading-engine — zsh</span></div>
    <div class="term-body">{term_lines}</div>
    <div class="chart">
      <div class="chart-head"><span>equity · illustrative</span><b>▲ trending</b></div>
      <svg viewBox="0 0 420 130" preserveAspectRatio="none" aria-hidden="true">
        <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#4ADE80" stop-opacity=".28"/><stop offset="1" stop-color="#4ADE80" stop-opacity="0"/>
        </linearGradient></defs>
        <path class="area" d="{area}" fill="url(#g)"/>
        <path class="curve" d="{line}" pathLength="1" fill="none" stroke="#4ADE80" stroke-width="2" stroke-linejoin="round"/>
      </svg>
    </div>
  </div>
</div></header>

<div class="ticker"><div class="ticker-track">{ticker}</div></div>
""")

# -------------------------------------------------------------------------- about
page("""
<section class="sec" id="about"><div class="wrap about">
  <div class="reveal">
    <div class="label">01 / About</div>
    <h2>Engineer by training.<br>Quant by trade.</h2>
    <p>I started in <b>mechanical engineering</b>, learning to model systems and respect constraints. An
      <b>MBA in Finance &amp; Analytics at IIM Amritsar</b> pointed that toolkit at markets: derivatives pricing,
      portfolio and risk management, valuation.</p>
    <p>Today I own the full loop at <b>Cloudcraftz AI</b>: from a hypothesis, to a backtest with realistic costs,
      to a live strategy with Greeks-aware hedging, circuit breakers and a dashboard watching every position.</p>
    <p>I like problems where the maths, the code and the P&amp;L all have to be right at the same time.</p>
  </div>
  <div class="stats reveal">
    <div class="stat"><div class="n">30<small>%</small></div><div class="d">ROI on an MCX crude-oil options strategy</div></div>
    <div class="stat"><div class="n">90<small>%</small></div><div class="d">less manual work after shipping the OptiStream pipeline</div></div>
    <div class="stat"><div class="n">80<small>%</small></div><div class="d">less manual effort on trade reconciliation</div></div>
    <div class="stat"><div class="n">49<small>×106</small></div><div class="d">instruments × trading days of minute data backtested</div></div>
  </div>
</div></section>
""")

# --------------------------------------------------------------------------- work
projects = [
    ("30% ROI", "Options strategy", "Crude Oil Mean-Reversion",
     "VWAP mean-reversion and Bollinger-squeeze signals on MCX crude options, with volatility and trend filters and delta-targeted strike selection.",
     ["Python", "Options", "MCX"]),
    ("ATR × IV z-score", "Options strategy", "Volatility-Regime Straddle",
     "ATM straddles sized by regime, using an ATR fast/slow ratio and intraday IV z-score, with spot-move circuit breakers and daily loss limits.",
     ["Volatility", "Sizing", "Risk limits"]),
    ("Δ Γ ν  live", "Risk", "Adaptive Hedging Framework",
     "Monitors position Greeks in real time and rebalances on regime shifts or risk-limit breaches, cutting unhedged exposure in volatile sessions.",
     ["Greeks", "Delta hedging"]),
    ("−90% manual work", "Data engineering", "OptiStream",
     "End-to-end options pipeline computing implied vol and the full Greeks surface with Black-Scholes and binomial models, scheduled on GCP.",
     ["GCP", "BigQuery", "Cloud Scheduler"]),
    ("−80% recon effort", "Trade operations", "Automated Reconciliation",
     "Flags position breaks, slippage anomalies and execution shortfalls as they happen, replacing a manual end-of-day process.",
     ["Python", "Automation"]),
    ("30s refresh", "Monitoring", "Real-Time P&amp;L Dashboard",
     "Compiled Mojo backend for trade-log parsing and P&amp;L aggregation behind a Streamlit UI. Built end to end with Claude.",
     ["Mojo", "Streamlit", "Claude"]),
]
cards = "".join(
    f'<article class="card reveal"><div class="m">{m}</div><div class="c">{c}</div><h4>{t}</h4><p>{d}</p>'
    f'<div class="tags">{"".join(f"<span>{x}</span>" for x in tags)}</div></article>'
    for m, c, t, d, tags in projects
)

page(f"""
<section class="sec" id="work"><div class="wrap">
  <div class="label">02 / Selected work</div>
  <h2>Systems I've built</h2>
  <p class="lede">Production work at Cloudcraftz AI. The code is proprietary, so here's what each system does and what it changed.</p>

  <div class="feature reveal">
    <div class="feature-top">
      <div><div class="label">Flagship</div><h3>Event-Driven Trading Engine</h3>
        <p>One strategy codebase that runs as a backtest, in paper trading, or live against broker APIs, swapped through a pluggable adapter layer.</p></div>
      <span class="pill">Python · REST APIs · ML</span>
    </div>
    <div class="arch">
      <div class="node"><div class="t">Market data</div><div class="s">feeds · tick recorder</div></div>
      <div class="arrow">→</div>
      <div class="node"><div class="t">Strategy</div><div class="s">EMA · RSI · VWAP</div></div>
      <div class="arrow">→</div>
      <div class="node hot"><div class="t">Execution adapter</div>
        <div class="modes"><span>backtest</span><span>paper</span><span class="live">live</span></div></div>
      <div class="arrow">→</div>
      <div class="node"><div class="t">Broker + logs</div><div class="s">retries · alerts · P&amp;L</div></div>
    </div>
    <div class="facts">
      <div><b>NSE + MCX</b>Equities and commodities, with realistic transaction-cost modelling.</div>
      <div><b>49 instruments · 106 days</b>Momentum and mean-reversion strategies tested on minute data.</div>
      <div><b>Runs daily, unattended</b>Scheduled live and paper cycles with session logs and email alerts.</div>
    </div>
  </div>

  <div class="grid3">{cards}</div>
</div></section>
""")

# ------------------------------------------------------------------------ journey
journey = [
    ("now", "Jun 2025 — now", "Quantitative Analyst", "Cloudcraftz AI · Kolkata", True,
     "Building the trading stack end to end: backtesting engine, options strategies, Greeks pipeline, reconciliation and live monitoring."),
    ("", "2025", "Algorithmic Trading with Python, ML &amp; AWS", "Certification", False,
     "Sharpened strategy automation and cloud deployment."),
    ("", "Dec 2023 — Jul 2024", "Management Trainee, Finance &amp; Analytics", "K12 Techno Services · Bengaluru", False,
     "Due diligence on multi-crore deals using DCF and EV/EBITDA and P/E comps. Built a logistic-regression credit-default model, Power BI and SQL reporting, and time-series forecasts."),
    ("win", "2023", "3rd Place, InSight Out Valuation Competition", "IIM Amritsar", False,
     "Placed in the institute-wide valuation competition."),
    ("", "2021 — 2023", "MBA, Finance &amp; Analytics", "IIM Amritsar · 76.5%", False,
     "Financial modelling, derivatives pricing, portfolio and risk management. Plus Portfolio &amp; Risk Management at ISB."),
    ("", "2015 — 2019", "B.Tech, Mechanical Engineering", "Meghnad Saha Institute of Technology · 74.5%", False,
     "Where the habit of modelling systems mathematically started."),
]
rows = "".join(
    f'<div class="tl-row reveal {cls}"><div class="tl-when">{when}</div><div class="tl-node"></div>'
    f'<div class="tl-what"><h4>{title}{"<span class=badge>NOW</span>" if now else ""}</h4>'
    f'<div class="org">{org}</div><p>{desc}</p></div></div>'
    for cls, when, title, org, now, desc in journey
)

skills = {
    "Languages": ["Python", "C++", "Mojo", "R", "SQL", "Bash", "VBA"],
    "Quant libraries": ["NumPy", "Pandas", "SciPy", "Scikit-learn", "Plotly", "Matplotlib"],
    "Trading": ["Event-driven backtesting", "Momentum", "Mean-reversion", "Volatility modelling", "Broker APIs"],
    "Derivatives": ["Black-Scholes", "Binomial trees", "Implied vol", "Greeks", "Delta hedging", "Risk limits"],
    "Data science": ["Machine learning", "Time-series forecasting", "Regression", "Classification", "Feature engineering"],
    "Platforms": ["GCP · BigQuery", "Cloud Scheduler", "ETL", "Streamlit", "Power BI", "Tableau", "Git", "Linux", "Claude"],
}
skill_cells = "".join(
    f'<div class="skill"><h5>{g}</h5><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
    for g, items in skills.items()
)

page(f"""
<section class="sec" id="journey"><div class="wrap">
  <div class="label">03 / Journey</div>
  <h2>From engineering to markets</h2>
  <p class="lede">Six years from modelling machines to modelling markets.</p>
  <div class="tl">{rows}</div>
</div></section>

<section class="sec" id="skills"><div class="wrap">
  <div class="label">04 / Toolkit</div>
  <h2>What I work with</h2>
  <p class="lede">Tools I use every day to take a strategy from research to production.</p>
  <div class="skills reveal">{skill_cells}</div>
  <div class="certs">
    <div class="cert"><b>🥉 3rd Place</b> · InSight Out Valuation, IIM Amritsar</div>
    <div class="cert"><b>Algo Trading</b> · Python, ML &amp; AWS</div>
    <div class="cert"><b>ISB</b> · Portfolio &amp; Risk Management</div>
    <div class="cert"><b>Kaggle</b> · Python · ML · NLP</div>
  </div>
</div></section>

<section class="sec" id="lab" style="padding-bottom:28px"><div class="wrap">
  <div class="label">05 / Options lab</div>
  <h2>Price an option. Watch the Greeks move.</h2>
  <p class="lede">The same Black-Scholes and binomial maths behind OptiStream, live in your browser. Change the inputs below.</p>
</div></section>
""")

# ----------------------------------------------------------- options lab (native)
with st.container(key="lab"):
    with st.container(key="lab-inputs"):
        c = st.columns([1.1, 1, 1, 1.3, 1.3], gap="medium")
        kind = c[0].segmented_control("Type", ["Call", "Put"], default="Call") or "Call"
        S = c[1].number_input("Spot", 1.0, 200000.0, 24000.0, 50.0, format="%.0f")
        K = c[2].number_input("Strike", 1.0, 200000.0, 24200.0, 50.0, format="%.0f")
        days = c[3].slider("Days to expiry", 1, 180, 21)
        iv = c[4].slider("Implied vol %", 5.0, 80.0, 14.0, 0.5)

    kind = kind.lower()
    r, sigma, T = 0.065, iv / 100, days / 365
    g = {k: float(v) for k, v in quant.black_scholes(S, K, T, r, sigma, kind).items()}
    american = quant.binomial_crr(S, K, T, r, sigma, kind, steps=300, american=True)
    european = quant.binomial_crr(S, K, T, r, sigma, kind, steps=300, american=False)

    tiles = [("main", "Premium", f"{g['price']:,.2f}", "Black-Scholes"),
             ("", "Delta Δ", f"{g['delta']:+.3f}", "per 1 pt spot"),
             ("", "Gamma Γ", f"{g['gamma']:.5f}", "Δ change / pt"),
             ("", "Theta Θ", f"{g['theta']:,.2f}", "per day"),
             ("", "Vega ν", f"{g['vega']:,.2f}", "per 1 vol pt"),
             ("", "American", f"{american:,.2f}", "binomial · 300 steps")]
    st.html('<div class="sd"><div class="greeks">' + "".join(
        f'<div class="greek {c_}"><div class="g">{n}</div><div class="val">{v}</div><div class="h">{h}</div></div>'
        for c_, n, v, h in tiles) + "</div></div>")

    spots = np.linspace(S * 0.9, S * 1.1, 161)
    today = quant.black_scholes(spots, K, T, r, sigma, kind)["price"]
    payoff = np.maximum(spots - K, 0) if kind == "call" else np.maximum(K - spots, 0)
    fig = go.Figure()
    fig.add_scatter(x=spots, y=payoff, name="Payoff at expiry", line=dict(color="#5B6478", width=1.6, dash="dot"))
    fig.add_scatter(x=spots, y=today, name=f"Value today ({days}d)", line=dict(color="#4ADE80", width=2.6),
                    fill="tonexty", fillcolor="rgba(74,222,128,.08)")
    fig.add_scatter(x=[S], y=[g["price"]], mode="markers", name="Current", marker=dict(size=10, color="#4ADE80",
                    line=dict(color="#06080D", width=2)), showlegend=False)
    fig.add_vline(x=K, line=dict(color="#263045", dash="dash"), annotation_text="strike",
                  annotation_font=dict(color="#8A93A6", family="JetBrains Mono", size=11))
    fig.update_layout(height=340, margin=dict(l=8, r=8, t=36, b=8), paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)", font=dict(family="JetBrains Mono, monospace", size=11, color="#8A93A6"),
                      legend=dict(orientation="h", y=1.1, x=0), hovermode="x unified")
    fig.update_xaxes(gridcolor="#1A2130", zeroline=False, title=None)
    fig.update_yaxes(gridcolor="#1A2130", zeroline=False, title=None)
    st.plotly_chart(fig, config={"displayModeBar": False}, width="stretch")
    st.html(f'<div class="sd"><p class="lab-note">r = 6.5% · early-exercise premium '
            f'{american - european:+.2f} · vega and theta shown per vol point and per calendar day</p></div>')

# ------------------------------------------------------------------------ contact
page(f"""
<section class="sec" id="contact" style="padding-top:64px"><div class="wrap">
  <div class="contact reveal">
    <div class="label">06 / Contact</div>
    <h2>Let's talk markets.</h2>
    <p>Open to quant research, systematic trading and derivatives roles, and to a good conversation about volatility.</p>
    <div class="ctas">
      <a class="btn btn-solid" href="mailto:{EMAIL}">Email me</a>
      <a class="btn btn-line" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>
      <a class="btn btn-line" href="{CV_URL}" download="Saptarshi_Das_CV.pdf">Download CV</a>
    </div>
    <span class="email">{EMAIL}</span>
  </div>
  <div class="foot"><span>© 2026 {NAME}</span><span>Kolkata, India · Python &amp; Streamlit</span></div>
</div></section>
""")
