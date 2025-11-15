# Placeholder for LLM judge if needed in future
def judge(outputA, outputB):
    return 'A' if len(outputA['suggestions']) > len(outputB['suggestions']) else 'B'
