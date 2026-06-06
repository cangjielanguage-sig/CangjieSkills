# Rollout XS-OVERLAY

- Observation sources: `screenshot-overlay.svg` and `control-tree-overlay.json`.
- State: the control tree marks the submit button enabled, but the screenshot shows a semi-transparent overlay covering it.
- Failed action: clicking the button center is intercepted.
- Successful action: dismiss the overlay, re-observe the UI, then click the button center.
- Result: the confirmation panel appears.
- Critique: dismissing an overlay is useful only when current visual evidence shows that overlay; it must not become an unconditional step.
