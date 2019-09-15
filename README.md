# Installation

Install environment with `pipenv` if you don't have pipenv follow instructions on [Installing Pipenv](#installing-pipenv)

```bash
pipenv install
```

## Installing Pipenv

```bash
pip install pipenv --user
```

# Usage

You will need 3 values for running **Prospector**:
- CRMID: the `crm_id` from Novoleads API, a string like: `tcross-julio19`
- TOKEN: the `token` from Novoleads API, a string like: `i5rikwmtcTJxS35Lck2nxSFBVxeq2_j0`
- CARMODEL: the selected Car Model: `T-Cross`

```bash
pipenv run python prospector.py tcross-julio19 i5rikwmtcTJxS35Lck2nxSFBVxeq2_j0 T-Cross
```