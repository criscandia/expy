# Installation

Install environment with `pipenv`  or `poetry`

## Activate environment

```bash
poetry shell # or pipenv shell
```

# Usage

You will need 3 values for running **Prospector**:
- CRMID: the `crm_id` from Novoleads API, a string like: `tcross-julio19`
- TOKEN: the `token` from Novoleads API, a string like: `i5rikwmtcTJxS35Lck2nxSFBVxeq2_j0`
- CARMODEL: the selected Car Model: `T-Cross`
- --car-brand: the car manufacturer like `volkswagen`
- --url: the Novoleads server URL

```bash
./prospector.py tcross-julio19 i5rikwmtcTJxS35Lck2nxSFBVxeq2_j0 T-Cross
```