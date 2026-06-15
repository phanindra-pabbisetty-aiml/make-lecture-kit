import sys
import os

# Add the scripts directory to the path so we can import figstyle
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
import figstyle

figstyle.annotated_sequence(
    ["The", "weather", "is", "rainy"],
    title="NLG: Generating one word at a time",
    highlight=[3],
    arrows=[(2, 3, "fwd")],
    out=os.path.join(os.path.dirname(__file__), 'nlg_process.png')
)
