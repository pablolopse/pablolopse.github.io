PROFILE = {
    "name": "Pablo López Serna",
    "tagline": "Physicist → Quant. Master's in Financial Engineering & Innovation.",
    "bio": (
        "Physics graduate (University of Salamanca) moving into quantitative "
        "finance through a Master's in Financial Engineering and Innovation at UPM. Background in "
        "computational and statistical physics, now applied to market microstructure, derivatives "
        "pricing, and stochastic modeling."
    ),
    "email": "pmpls13@gmail.com",
    "github": "https://github.com/pablolopse",
    "linkedin": "https://www.linkedin.com/in/pablolopse/",
    "cv_pdf": "cv.pdf",
}

PROJECTS = [
    {
        "slug": "orderbook",
        "name": "Order Book Predictor — Neural Order Flow Forecasting",
        "repo": "https://github.com/pablolopse/orderbook_predictors",
        "tags": ["Python", "Keras/TensorFlow", "Market Microstructure"],
        "summary": (
            "A feed-forward neural network predicts short-term limit-order-book mid-price "
            "direction from multi-level bid/ask price-and-volume snapshots and recent order-flow "
            "history, benchmarked against linear and quadratic logistic regression baselines."
        ),
        "results": [
            "Regularized NN: 77.3% out-of-sample test accuracy (F1 76.4%) on a held-out 10,000-row set.",
            "Linear logistic regression baseline: 71.7% · Quadratic logistic regression: 73.4%",
            "Independently reproduced the original notebook's reported 0.7733 test accuracy (got 0.7734).",
        ],
        "hero_img": "assets/img/projects/orderbook_hero.png",
        "hero_caption": "Out-of-sample test accuracy across all five models.",
        "secondary_img": "assets/img/projects/orderbook_secondary.png",
        "secondary_caption": "NN training curves: an unstable run, an overfitting run, and the final dropout-regularized model.",
    },
    {
        "slug": "options",
        "name": "Options Pricer — Black-Scholes, Jump-Diffusion & Path-Dependent Models",
        "repo": "https://github.com/pablolopse/options_pricer",
        "tags": ["Python", "Monte Carlo", "PDE", "Variance Reduction", "Derivatives Pricing"],
        "summary": (
            "Prices European, American, and path-dependent (Asian) options seven ways — "
            "Black-Scholes and Merton jump-diffusion closed forms, a CRR binomial tree, an "
            "explicit finite-difference PDE solver, Longstaff-Schwartz Monte Carlo, and a "
            "variance-reduced Monte Carlo engine using antithetic variates — with analytic "
            "Greeks. The risk-free rate is pulled live from the 10-year Treasury yield."
        ),
        "results": [
            "Black-Scholes: 10.42 · American Binomial: 10.41 · American Finite-Difference: 10.41 · "
            "American LSM: 10.28 (spot=strike=100, T=1y, σ=0.20).",
            "Antithetic-variates variance reduction cuts Monte Carlo standard error by a "
            "consistent ~30% at matched path counts — equivalent to ~2x the paths for free.",
            "Arithmetic-average Asian call converges to ≈5.85, correctly below the vanilla "
            "European price of 10.43, reflecting the lower effective volatility of an averaged payoff.",
        ],
        "hero_img": "assets/img/projects/options_hero.png",
        "hero_caption": "Model comparison: Black-Scholes vs. jump-diffusion vs. binomial vs. PDE vs. LSM.",
        "secondary_img": "assets/img/projects/options_secondary.png",
        "secondary_caption": "Antithetic-variates Monte Carlo: ~30% lower standard error than plain Monte Carlo at every path count.",
    },
    {
        "slug": "ising",
        "name": "Monte Carlo Simulation of the 2D Ising Model",
        "repo": "https://github.com/pablolopse/ising-model-simulation",
        "tags": ["Fortran", "Monte Carlo", "Statistical Physics"],
        "summary": (
            "A from-scratch Fortran implementation of three Monte Carlo algorithms "
            "(Metropolis, Glauber heat-bath, Wolff cluster) for the 2D Ising model, used to "
            "study critical slowing down, algorithmic ergodicity, and the ferromagnetic phase "
            "transition."
        ),
        "results": [
            "Finite-size scaling (Binder cumulant crossings) locates the critical temperature "
            "within ~0.15% of the exact Onsager solution (2.26919).",
            "Metropolis: Tc = 2.27259 · Glauber: Tc = 2.26932 · Wolff: Tc = 2.27196",
            "Heat capacity and susceptibility both sharpen near Tc as system size L grows — the "
            "correct finite-size signature of a continuous phase transition.",
        ],
        "hero_img": "assets/img/projects/ising_hero.png",
        "hero_caption": "Binder cumulant crossing used to extract the critical temperature.",
        "secondary_img": "assets/img/projects/ising_energy.png",
        "secondary_caption": "Energy per spin vs. temperature across system sizes.",
    },
    {
        "slug": "ljliquids",
        "name": "Lennard-Jones Fluid: g(r) via Monte Carlo & Liquid-State Theory",
        "repo": "https://github.com/pablo-05/LJLiquids",
        "tags": ["Fortran", "Monte Carlo", "Statistical Physics", "Liquid-State Theory"],
        "summary": (
            "Computed the radial distribution function g(r) of a Lennard-Jones fluid two "
            "independent ways — a 3D Metropolis Monte Carlo simulation and an iterative "
            "Ornstein-Zernike solution under Percus-Yevick and Hypernetted-Chain closures — "
            "across gas, near-critical, and liquid states, cross-validating theory against "
            "simulation. Collaborative project for an Advanced Statistical Physics course."
        ),
        "results": [
            "Gas state (ρ*=0.05, T*=0.95): both PY and HNC closures match Monte Carlo almost "
            "exactly (RMSE 0.017 and 0.029).",
            "Liquid state (ρ*=0.75, T*=0.95): both closures visibly overshoot the first "
            "coordination shell — a well-known, physically expected breakdown of integral-"
            "equation theory at high packing density, reproduced quantitatively (HNC RMSE "
            "0.075 vs PY 0.084).",
            "Full vs. cut-and-shifted potential g(r) curves overlap almost perfectly at the "
            "same state point, confirming truncation barely affects local structure.",
        ],
        "hero_img": "assets/img/projects/ljliquids_hero.png",
        "hero_caption": "Theory vs. Monte Carlo g(r) in the liquid regime — closures overshoot the first peak.",
        "secondary_img": "assets/img/projects/ljliquids_secondary.png",
        "secondary_caption": "Full vs. cut-and-shifted potential: near-identical g(r) at the same state point.",
    },
    {
        "slug": "nuclear",
        "name": "Nuclear Spectroscopy Lab",
        "repo": "https://github.com/pablolopse/nuclear-lab",
        "tags": ["Fortran", "Python", "Nuclear Physics"],
        "summary": (
            "Analysis code for two university nuclear-physics lab sessions: a Compton-scattering "
            "coincidence experiment and gamma-ray spectroscopy (NaI/HPGe detectors). A "
            "hand-written Fortran routine fits Gaussian peaks on multichannel-analyzer spectra by "
            "linearizing the fit with a log-parabola transform."
        ),
        "results": [
            "K-40 calibration peak (1460.8 keV): centroid 206.37 ch, FWHM 8.67 ch, area 88,664.8 "
            "counts — Fortran fit reproduced exactly.",
            "Background-subtracted Mg-4 spectrum peak fit: centroid 19.46 ch, FWHM 2.99 ch — "
            "matched exactly on independent re-run.",
        ],
        "hero_img": "assets/img/projects/nuclear_hero.png",
        "hero_caption": "Background-subtracted gamma spectrum of the Mg-4 sample.",
        "secondary_img": "assets/img/projects/nuclear_secondary.png",
        "secondary_caption": "Compton coincidence characterization spectrum (Co-60).",
    },
]

EDUCATION = [
    {
        "school": "Technical University of Madrid (UPM), Spain",
        "degree": "Master in Financial Engineering and Innovation",
        "period": "Sep 2026 – Expected Jun 2027",
        "details": [
            "Advanced curriculum: Game Theory, Advanced Probability, Financial Mathematics, Machine Learning.",
            "Core modules and seminars led by industry practitioners and quantitative finance experts.",
        ],
    },
    {
        "school": "University of Salamanca, Spain",
        "degree": "B.Sc. in Physics",
        "period": "Sep 2022 – Jul 2026",
        "details": [
            "Honours in Computational Physics and Statistical Physics.",
            "Coursework: Numerical Methods, Differential Equations, Statistical Physics, Quantum Mechanics.",
        ],
    },
    {
        "school": "Imperial College London",
        "degree": "Summer School in Machine Learning, Statistics, and Trading Systems",
        "period": "Jun 2025 – Jul 2025",
        "details": [
            "Selective programme integrating machine learning, stochastic processes, and quantitative modeling for financial markets.",
        ],
    },
]

EXPERIENCE = [
    {
        "role": "Interim Quant Analyst",
        "org": "Coral Homes / Lone Star Funds",
        "location": "Madrid, Spain",
        "period": "Jul 2025 – Sep 2025",
        "details": [
            "Conducted quantitative analysis on a REO land portfolio using Python and Pandas.",
            "Developed statistical models to identify asset demand dynamics and optimize disposition strategies.",
            "Delivered dashboards and analytical forecasts for portfolio risk and performance.",
        ],
    },
    {
        "role": "Freelance Software Developer",
        "org": "Independent Contractor",
        "location": "",
        "period": "Feb 2022 – Present",
        "details": [
            "Built automation, data-analytics pipelines, and backend infrastructure for clients in tech and finance.",
            "Designed scalable solutions using Python, SQL, and AWS; improved data processing throughput by 40%+.",
        ],
    },
    {
        "role": "Lead Software Engineer",
        "org": "ViralPlan",
        "location": "Barcelona, Spain",
        "period": "Feb 2023 – Jan 2024",
        "details": [
            "Architected software systems and optimized development lifecycles for analytics/automation tools.",
            "Led a remote engineering team; reduced API latency by 35%.",
            "Designed internal dashboards for data-driven business decisions.",
        ],
    },
    {
        "role": "Core Developer",
        "org": "Smart Crypto",
        "location": "Barcelona, Spain",
        "period": "Oct 2022 – May 2023",
        "details": [
            "Developed blockchain-integrated financial simulation tools and quantitative pricing models.",
            "Researched tokenomics, market mechanisms, and algorithmic designs for DeFi.",
        ],
    },
]

AWARDS = [
    "RSEF – GEFES Research Awards for Undergraduate Students (2026)",
    "University of Salamanca Magna Cum Laude Award for Academic and Professional Excellence (2025)",
]

SKILLS = {
    "Programming & Tools": ["Python (NumPy, Pandas, scikit-learn, TensorFlow/Keras)", "Fortran", "C++", "SQL", "Git", "AWS", "Docker"],
    "Quantitative Methods": ["Probability Theory", "Stochastic Calculus", "Monte Carlo Methods", "Optimization", "Time Series Analysis", "Game Theory"],
    "Languages": ["Spanish (Native)", "English (Full Professional)", "French (Elementary)", "Italian (Elementary)"],
}

INTERESTS = [
    "Volunteer and mentor through Pyfano, supporting children with cancer.",
    "Profitable poker player specializing in 3-max Hyper-Turbo (Spin & Go) formats.",
    "Chess player with a strong focus on game theory.",
    "Local darts league player, horse rider and breeder (Yeguada Alora).",
]
