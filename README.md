# Data Science Fundamentals Assessment

Repository: https://github.com/appureddy1102-cloud/data-science-fundamentals-assessment-professional

A reproducible, educational project covering Python, data types, descriptive and inferential statistics, exploratory analysis, six visualizations, model evaluation and responsible practice. The data are synthetic. Classification and regression examples use fixed hypothetical predictions; no machine-learning model is fitted.

## Objectives and topics
Learn Python fundamentals, represent data correctly, calculate and interpret statistics, clean and summarize CSV data, compare chart types, understand model-validation and evaluation metrics, and document reproducible and ethical workflows. See the report for worked calculations and the requirement-by-requirement audit in `QUALITY_AUDIT.md`.

## Data and findings
See [data/README.md](data/README.md) for the synthetic dataset and CC0 license. Raw: 122 records, 2 exact duplicates, 3 missing unit values; cleaned: 120 records. Simulated gross revenue is $16,485, including $9,295 electronics, $4,550 home and $2,640 books. Mean revenue is $137.38 and median $120. January is $5,160; April $3,850. Category prices are fixed by construction: these patterns are not real-world conclusions.

## Environment and execution
The completed notebook was executed under Python 3.13.16; exact analysis-library versions are in `requirements.txt` and `outputs/analysis_summary.json`. On Windows PowerShell, install Python 3.13 and from the project root:
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/fundamentals_examples.py
python -m notebook
```
Open `notebooks/data_science_fundamentals.ipynb` and select Kernel → Restart Kernel and Run All Cells. The notebook accepts the project root or notebooks directory as its working directory, and overwrites files in outputs. For automated execution use `python -m jupyter nbconvert --to notebook --execute --inplace notebooks/data_science_fundamentals.ipynb`. On macOS/Linux use `python3.13 -m venv .venv` then `source .venv/bin/activate`. Windows installation was not tested here.

**Troubleshooting:** if PowerShell blocks activation, invoke `.venv\Scripts\python.exe -m pip` and `.venv\Scripts\python.exe -m notebook` directly. If an import fails, select the same environment as the notebook kernel; register it with `python -m ipykernel install --user --name fundamentals --display-name "Python (fundamentals)"`. If CSV lookup fails, keep the project structure and start from the project root or notebooks folder. If `py` is missing, install the Python launcher or use Python's full path.

## Contents
```
data/README.md, data/synthetic_sales.csv
notebooks/data_science_fundamentals.ipynb
scripts/fundamentals_examples.py
outputs/cleaned_sales.csv, analysis_summary.json, figures/
report/Data_Science_Fundamentals_Report.docx
requirements.txt, QUALITY_AUDIT.md, VIVA_QUESTIONS.md
```

## Upload to GitHub
Create an empty repository, then in the project directory run `git init`, `git add .`, `git commit -m "Add fundamentals assessment"`, `git branch -M main`, `git remote add origin <your-repository-url>` and `git push -u origin main`. Authenticate with GitHub's supported secure method, not a token pasted into code, a URL, or a committed file. Review data and files before publication.

## References
- Python tutorial and style: https://docs.python.org/3/tutorial/ ; https://peps.python.org/pep-0008/
- NumPy and Pandas: https://numpy.org/doc/ ; https://pandas.pydata.org/docs/
- SciPy statistics: https://docs.scipy.org/doc/scipy/reference/stats.html
- Matplotlib and Seaborn: https://matplotlib.org/stable/ ; https://seaborn.pydata.org/
- Scikit-learn metrics and cross-validation: https://scikit-learn.org/stable/modules/model_evaluation.html ; https://scikit-learn.org/stable/modules/cross_validation.html
- NIST handbook: https://www.itl.nist.gov/div898/handbook/
