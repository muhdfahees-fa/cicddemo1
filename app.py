from flask import Flask

app = Flask(__name__)

VERSION = "v1"


@app.route("/")
def home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo App</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }}

        .container {{
            text-align: center;
            padding: 50px;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 60px 50px;
            max-width: 600px;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5);
            animation: fadeIn 1s ease-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .icon {{
            font-size: 64px;
            margin-bottom: 20px;
            animation: pulse 2s ease-in-out infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #00d2ff, #7b2ff7, #ff6ad5);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient 3s ease infinite;
            margin-bottom: 12px;
        }}

        @keyframes gradient {{
            0% {{ background-position: 0% center; }}
            50% {{ background-position: 100% center; }}
            100% {{ background-position: 0% center; }}
        }}

        .version {{
            display: inline-block;
            background: linear-gradient(135deg, #7b2ff7, #00d2ff);
            color: white;
            padding: 8px 24px;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 1px;
            margin-bottom: 35px;
        }}

        .pipeline {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            flex-wrap: wrap;
            margin-bottom: 35px;
        }}

        .stage {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #c0c0e0;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.3s;
        }}

        .stage:hover {{
            background: rgba(123, 47, 247, 0.3);
            border-color: #7b2ff7;
            color: white;
            transform: translateY(-2px);
        }}

        .arrow {{
            color: #555;
            font-size: 1rem;
        }}

        .tools {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }}

        .tool {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }}

        .tool-icon {{
            width: 50px;
            height: 50px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            transition: transform 0.3s;
        }}

        .tool-icon:hover {{
            transform: scale(1.15);
        }}

        .tool-git {{ background: linear-gradient(135deg, #f05032, #e04020); }}
        .tool-docker {{ background: linear-gradient(135deg, #2496ed, #1a7fd4); }}
        .tool-aws {{ background: linear-gradient(135deg, #ff9900, #e88800); }}
        .tool-github {{ background: linear-gradient(135deg, #6e40c9, #553098); }}

        .tool-label {{
            color: #888;
            font-size: 0.7rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .status {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            color: #4ade80;
            font-size: 0.9rem;
        }}

        .status-dot {{
            width: 10px;
            height: 10px;
            background: #4ade80;
            border-radius: 50%;
            animation: blink 1.5s ease-in-out infinite;
        }}

        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.3; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="icon">&#9881;</div>
            <h1>CI/CD Pipeline Demo</h1>
            <div class="version">{VERSION}</div>

            <div class="pipeline">
                <span class="stage">Source</span>
                <span class="arrow">&#9654;</span>
                <span class="stage">Build</span>
                <span class="arrow">&#9654;</span>
                <span class="stage">Test</span>
                <span class="arrow">&#9654;</span>
                <span class="stage">Publish</span>
                <span class="arrow">&#9654;</span>
                <span class="stage">Deploy</span>
                <span class="arrow">&#9654;</span>
                <span class="stage">Verify</span>
            </div>

            <div class="tools">
                <div class="tool">
                    <div class="tool-icon tool-git">&#128736;</div>
                    <span class="tool-label">Git</span>
                </div>
                <div class="tool">
                    <div class="tool-icon tool-docker">&#128051;</div>
                    <span class="tool-label">Docker</span>
                </div>
                <div class="tool">
                    <div class="tool-icon tool-aws">&#9729;</div>
                    <span class="tool-label">AWS EC2</span>
                </div>
                <div class="tool">
                    <div class="tool-icon tool-github">&#128640;</div>
                    <span class="tool-label">Actions</span>
                </div>
            </div>

            <div class="status">
                <span class="status-dot"></span>
                Service is running
            </div>
        </div>
    </div>
</body>
</html>"""


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
