from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def execute_command(command, language):
    try:
        if language == 'python':
            result = subprocess.run(['python', '-c', command], capture_output=True, text=True)
        elif language == 'csharp':
            # Execute C# code (requires a setup with .NET)
            pass
        elif language == 'cpp':
            # Execute C++ code (requires appropriate compiler)
            pass
        # Add handlers for other languages...
        else:
            return 'Unsupported language'

        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

@app.route('/execute', methods=['POST'])
def execute():
    command = request.json['command']
    language = request.json.get('language', 'python')  # Default to Python
    output = execute_command(command, language)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
