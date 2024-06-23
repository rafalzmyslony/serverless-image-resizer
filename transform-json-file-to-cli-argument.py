import json
import sys

command_before = 'aws sqs set-queue-attributes --queue-url $QUEUE_URL --attributes'
command_after = ''
def escape_json(json_object):
    json_str = json.dumps(json_object)
    escaped_json_str = json_str.replace('"', '\\"')
    return f'{{"Policy": "{escaped_json_str}"}}'

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    
    try:
        with open(json_file_path, 'r') as file:
            json_object = json.load(file)
            escaped_policy = escape_json(json_object)
            print(escaped_policy)
            print()
            print()
            print()
            print(command_before, '\'',escaped_policy, '\'')
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
