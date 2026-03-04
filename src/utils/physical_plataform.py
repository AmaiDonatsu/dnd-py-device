def we_are_in_SBC():
    try:
        model = get_SBC_model()
        return "Unknown" not in model
    except:
        return False
    
def get_SBC_model():
    try:
        with open("/proc/device-tree/model", "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading SBC model: {e}")
        return "Unknown"