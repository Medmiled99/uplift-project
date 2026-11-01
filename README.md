# When the offline metric lies

Work in progress. Does the model with the best offline score also create the most extra conversions? This project analyses a real randomised advertising experiment to find out.

## Questions

1. Did the ads work? How big is the effect, and is it big enough to matter?
2. How many users would a future test need?
3. Does the model with the best AUC also bring the most incremental conversions?
4. Which metric should a team optimise?

## Data

[Criteo Uplift Prediction Dataset](https://ailab.criteo.com/criteo-uplift-prediction-dataset/), v2.1 (13,979,592 rows). It is not stored in this repo.

- Download: https://huggingface.co/datasets/criteo/criteo-uplift
- Save it as `~/data/criteo-uplift/criteo-uplift-v2.1.csv.gz`, or set `CRITEO_DATA_DIR` to another folder.

Limits of the data:

- It comes from web advertising, not mobile games.
- It pools several experiments and was sub-sampled non-uniformly for privacy, so the rates are not Criteo's real business rates.
- The features are anonymised, so segments can't be given a business meaning.

Citation: Diemert, E., Betlei, A., Renaudin, C., & Amini, M.-R. (2018). *A Large Scale Benchmark for Uplift Modeling*. AdKDD and TargetAd Workshop, KDD 2018. Licensed under CC BY-NC-SA 4.0.

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/01_ab_test.ipynb
```

## Results

To be added.
