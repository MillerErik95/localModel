## Prerequisites

- [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html#mamba-install) (Preferred)
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [pip](https://pip.pypa.io/en/stable/installation/) for alternative installation.

## Setup Mamba Environment (Recommended for Development)

For easiest installation and reproducibility in development, it’s recommended to use Mamba to manage your environment:

```bash
mamba env create -f conda.yaml
mamba activate model
```

## Alternative Setup Using `requirements.txt`

If you prefer to use `pip` or cannot use Mamba, you can install the dependencies from the `requirements.txt` file:

1. Create and activate a new virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Preparing .env
Create .env file in project folder

```
Model/              <- Project root
├── source/
│   └── main.py
└── .env                <- Create .env
```

and add the necessary variables.
```
ANTHROPIC_API_KEY = 
```
