"""
This test is needed to test the rendering of messages with emojis.
"""
from messages.messages import Messages

messages = Messages('tests/configs/messages.json')

TARGET_RESULT = (
    "Hi, <b>pytest</b>! ✋\n"
    "Access for your account - allowed 🔓"
)

def test_render_template():
    """
    Functions for approving the result between TARGET_RESULT and the response from the module.
    """
    response = messages.render_template('test_message', username='pytest')
    assert response == TARGET_RESULT

if __name__ == "__main__":
    test_render_template()
    print("Rendering template - passed")
