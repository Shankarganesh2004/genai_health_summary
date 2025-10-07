import yaml

with open("utils/config.yaml", "r") as f:
    config = yaml.safe_load(f)

def interpret_values(df):
    result = {}
    for test, value in df.iloc[0].items():
        rules = config.get(test, {})
        normal = rules.get("normal_range", [0, 999])
        if value < normal[0]:
            status = "Low"
        elif value > normal[1]:
            status = "High"
        else:
            status = "Normal"
        result[test] = {"value": value, "status": status, "risk": rules.get("risk", {}).get(status, "None")}
    return result