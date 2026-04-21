"""
3GPP TDL Channel Models
Author: Pujan Thapa Magar

Practicing Python dictionaries using 3GPP TDL channel models.
TDL models define delay spread and LOS conditions for 5G NR simulations.
"""

tdl_models = {
    "TDL-A": {"delay_spread_ns": 30,  "los": False},
    "TDL-B": {"delay_spread_ns": 100, "los": False},
    "TDL-C": {"delay_spread_ns": 300, "los": False},
    "TDL-D": {"delay_spread_ns": 300, "los": True},
    "TDL-E": {"delay_spread_ns": 1000, "los": True}
}

# printing each model with its parameters
for model, params in tdl_models.items():
    los = "Yes" if params["los"] else "No"
    print(f"{model} - delay spread: {params['delay_spread_ns']} ns, LOS: {los}")

