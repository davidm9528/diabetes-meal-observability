# Diabetes Observability & Logging System

This project is a structured system for tracking, analyzing, and responding to blood glucose patterns using CGM data and manual logging. It is designed to help people with Type 1 Diabetes identify trends, fine-tune insulin usage, and automate insights for better daily management.

---

## Log Guide Version: 1.1

Last Updated: 2025-05-06

### Default CGM Response Format

```
[Time] | BG: [value] [arrow] | Alarm Set: [level]
[Brief, actionable notes]
```

**Example:**

```
21:49 | BG: 7.1 ↑ | Alarm Set: 10.0
That’s fine. 10 mmol/L is a solid ceiling — no action needed unless you hit it.
```

### Example CGM Responses

- **Stable post-meal:**  
  `14:45 | BG: 7.4 → | Alarm Set: 10.0`  
  No correction needed. Monitor again in 1h for delayed rise.

- **Climbing midday:**  
  `15:18 | BG: 10.6 ↑ | Alarm Set: 11.0`  
  Could be delayed spike. Reassess in 30 min.

- **Borderline hypo:**  
  `17:11 | BG: 4.5 ↓ | Alarm Set: 3.9`  
  Take 5–10g carbs. Recheck in 15 min.

- **Overnight risk:**  
  `02:30 | BG: 4.3 → | Alarm Set: 3.9`  
  Stay alert but no immediate action.

- **Post-correction rise:**  
  `19:10 | BG: 8.9 ↑ | Alarm Set: 10.0`  
  Let it ride unless it breaches 10.

---

## Meal Logging Format

```
DATE: YYYY-MM-DD
TIME: HH:MM
MEAL: [Meal description]
MACROS: [Carbs=Xg, Protein=Yg, Fat=Zg]
PRE-BG: X.X mmol/L
WAIT AFTER BOLUS: X min
MEAL TYPE TAG (MTT): [HPNC / HFHP / MMX / UL / EXP]
NOTES: [BG readings, corrections, symptoms, etc.]
```

**Meal Tags:**

- HPNC – High Protein, No Carb
- HFHP – High Fat, High Protein
- MMX – Mixed Meal
- UL – Usual Lunch
- EXP – Experimental

---

## Alarm Strategy Guidelines

| Level         | Threshold | Action                                           |
| ------------- | --------- | ------------------------------------------------ |
| LOW           | 4.5       | Prepare 5–10g fast-acting carbs                  |
| URGENT LOW    | 3.9       | Take 15g carbs, recheck in 15 min                |
| CRITICAL LOW  | 3.5       | Take 20g fast-acting carbs + monitor             |
| HIGH          | 10.0      | Monitor, correct if rising and no IOB            |
| EARLY HIGH    | 8.5       | Useful for tight post-meal tracking              |
| CRITICAL HIGH | 15.0      | Correct immediately + hydrate, watch for ketones |

---

## Protocols

### Severe Hypoglycemia (≤2.9 mmol/L)

- Take **20g fast-acting carbs**
- Rest and recheck in 15 min
- Repeat if still <3.9
- Once >5.0 and stable, take slow-acting carbs if insulin is on board
- Seek help if unresolved after 2 treatments

### Severe Hyperglycemia (≥15.0 mmol/L)

- Hydrate with 300–500ml water
- Take correction insulin if no IOB
- Avoid food until BG <10
- If >17.0, hydrate aggressively and recheck within 90 min
- Seek help if no drop or symptoms worsen

---

## File List

- `Diabetes_Log_Guide_v1.1.json` – full structured log guide
- `Diabetes_Log_Guide_v1.1.txt` – human-readable version
- `Severe_Hypoglycemia_Protocol.json` – emergency low protocol
- `Severe_Hyperglycemia_Protocol.json` – emergency high protocol

---

## Notes

- Logging is structured to allow export for GitHub or analysis
- Designed for reuse across projects and automation

---

## FastAPI Integration

This project includes a FastAPI backend to expose endpoints for diabetes observability, such as submitting CGM logs or retrieving protocol data.

### Project Structure (API portion)

```
app/
├── main.py                # FastAPI entrypoint
├── api/endpoints.py       # Route definitions
├── models/schemas.py      # Pydantic data models
├── services/log_handler.py# Core logic for saving logs
├── core/config.py         # Placeholder for future config/env
```

### Endpoints

- `GET /home` — main page to log glucose (will remove in future)
- `GET /meal` — log a meal entry
- `POST /log` — accepts a log entry and saves it to JSON

### Run the App

```bash
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
