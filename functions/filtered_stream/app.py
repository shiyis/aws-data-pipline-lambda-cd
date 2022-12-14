from filtered_stream import get_rules,delete_all_rules, set_rules,get_stream

def lambda_handler(event, context):
    rules = get_rules()
    delete = delete_all_rules(rules)
    set_rule = set_rules(delete)
    data = get_stream(set_rule)
    return data
