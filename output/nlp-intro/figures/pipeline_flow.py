import sys
import os

# Add the scripts directory to the path so we can import figstyle
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
import figstyle

# We use the built-in `flow` helper from figstyle
figstyle.flow(
    steps=["Raw Text\n\"Book a flight\"", "Tokenization", "Intent/Entity\nExtraction", "Structured Data\n{Intent: Book}"],
    title="The NLP Pipeline",
    direction="lr",
    out=os.path.join(os.path.dirname(__file__), 'pipeline_flow.png')
)
