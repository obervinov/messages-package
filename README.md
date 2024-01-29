# Messages Package
[![Release](https://github.com/obervinov/messages-package/actions/workflows/release.yaml/badge.svg)](https://github.com/obervinov/messages-package/actions/workflows/release.yaml)
[![CodeQL](https://github.com/obervinov/messages-package/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/obervinov/messages-package/actions/workflows/github-code-scanning/codeql)
[![PR](https://github.com/obervinov/messages-package/actions/workflows/pr.yaml/badge.svg?branch=main&event=pull_request)](https://github.com/obervinov/messages-package/actions/workflows/pr.yaml)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/obervinov/messages-package?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/obervinov/messages-package?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/obervinov/messages-package?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/obervinov/messages-package?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/obervinov/messages-package?style=for-the-badge)

## <img src="https://github.com/obervinov/_templates/blob/main/icons/book.png" width="25" title="about"> About this project
This package helps to easily and quickly generate beautiful messages for telegram bots using templates described in json.

## <img src="https://github.com/obervinov/_templates/blob/main/icons/github-actions.png" width="25" title="github-actions"> GitHub Actions
| Name  | Version |
| ------------------------ | ----------- |
| GitHub Actions Templates | [v1.0.12](https://github.com/obervinov/_templates/tree/v1.0.12) |


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Supported functions
- Rendering a line with progress bar
- Rendering a line with emoji
- Rendering a simple string

## <img src="https://github.com/obervinov/_templates/blob/v1.0.5/icons/build.png" width="25" title="build"> Environment variables
| Variable  | Description | Default value |
| ------------- | ------------- | ------------- |
| `MESSAGES_CONFIG` | Json file with templates for rendering messages. [Example](tests/configs/messages.json) | `configs/messages.json` |


## <img src="https://github.com/obervinov/_templates/blob/main/icons/stack2.png" width="20" title="install"> Installing with Poetry
```bash
tee -a pyproject.toml <<EOF
[tool.poetry]
name = myproject"
version = "1.0.0"

[tool.poetry.dependencies]
python = "^3.10"
messages = { git = "https://github.com/obervinov/messages-package.git", tag = "v1.0.3" }

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

poetry install
```

## <img src="https://github.com/obervinov/_templates/blob/main/icons/config.png" width="25" title="usage"> Usage examples
### Simple message with emoji
1. Creating _configs/messages.json_ and adding an example template
   - all emojis should be wrapped in `:`
   - all variables must be specified in the same form as in your code
```json
{
    "templates": {
        "hello_message": {
            "text": "Hi, <b>{0}</b>! {1}\nAccess for your account - allowed {2}",
            "args": ["username", ":raised_hand:", ":unlocked:"]
        }
    }
}
```

```python
# Import module
from messages import Messages

# Create instance
messages = Messages()

# Rendering and getting messages
print(
    messages.render_template(
        template_alias='hello_message',
        username="obervinov"
    )
)
```

_output result_
```python
Hi, <b>obervinov</b>! ✋
Access for your account - allowed 🔓
```

### Simple message with progress bar
1. Creating _configs/messages.json_ and adding an example template
   - all emojis should be wrapped in `:`
   - all variables must be specified in the same form as in your code
```json
{
    "templates": {
        "queue_message": {
            "text": "{0} Messages from the queue have already been processed\n{1}",
            "args": [":framed_picture:", "progressbar"]
        }
    }
}
```

```python
# Import module
from messages import Messages

# Create instance
messages = Messages()

# Render and get messages with progress bar
print(
    messages.render_template(
        template_alias='queue_message',
        progressbar=messages.render_progressbar(
            total_count=100,
            current_count=19
        )
    )
)
```

_output result_
```python
🏞 Messages from the queue have already been processed
[◾◾◾◾◾◾◾◾◾◾◾◾◾◾◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻◻◻◻]19%
```
