"""
This test is needed to test the rendering of progressbar with emojis.
"""
from messages.messages import Messages

messages = Messages('tests/configs/messages.json')

TARGET_RESULT = (
    "\r[◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾"
    "◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️"
    "◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️◻️]19%"
)


def test_render_progressbar():
    """
    Functions for approving the result between TARGET_RESULT and the response from the module.
    """
    response = messages.render_progressbar(100, 19)
    assert response == TARGET_RESULT
