# Screenshot-Driven UI Validation

Use this workflow only when the request supplies a screenshot, mockup, or other visual reference.

## Required Model Route

- Give reference-image inspection and final screenshot comparison to an image-capable agent.
- A text-only coding model may handle API lookup, source edits, builds, and key/text assertions, but it must not claim that the UI matches an image it cannot inspect.
- Keep the image-capable evaluation independent: pass the raw reference, capture, task, and Skills—not an intended verdict or hidden source implementation.

## Workflow

1. Copy the reference into the isolated task directory and treat it as immutable evidence.
2. Inspect it visually and write a short implementation inventory: hierarchy, visible text, dominant colors, major bounds, spacing rhythm, typography hierarchy, corner radii, and repeated rows/cards.
3. Implement stable business keys and exact visible text before tuning appearance.
4. Build and capture on the same device class, orientation, and resolution used for every iteration. For pure Cangjie cold start, use `--wait 8 --foreground-retries 2`.
5. Before accepting a capture as a visual iteration, require both the target bundle in the foreground and at least one expected application root key or distinctive business string in `ui_summary.md`. A PNG containing only the status/navigation bars, launcher, start-window icon, splash surface, or system error UI is a runtime failure—not visual evidence. Diagnose launch/install/log state and recapture without advancing the iteration number.
6. Preserve valid captures as `visual_iteration_1/`, `visual_iteration_2/`, and so on. Inspect `screenshot.png` plus `ui_summary.md`; do not dump raw `layout.json`.
7. Have the image-capable agent compare reference and capture side by side. Fix the largest structural mismatch first, then geometry/spacing, color/surface, typography, and small details.
8. Stop when the task's acceptance threshold is met or after three bounded visual iterations; report remaining mismatches honestly.

## Comparison Rubric

Record one verdict for each category:

| Category | Check |
| --- | --- |
| Content | Visible strings, row count, ordering, and states match |
| Structure | Major sections and nesting have the same visual hierarchy |
| Geometry | Margins, widths, heights, alignment, spacing, and corner radii are close |
| Color | Backgrounds, surfaces, accents, and status colors are close |
| Typography | Relative size, weight, color, and alignment are close |
| Runtime | Target bundle is foreground and required interactions still pass |

System status/navigation bars, current time, radio icons, font rasterization, and emulator-specific antialiasing may differ. Separate those from application-content mismatches.

## Evidence Contract

The final handoff must include:

- reference image path;
- final emulator screenshot path;
- application source and HAP path;
- iteration count;
- visual comparison by an image-capable agent;
- business key/text assertion results;
- known remaining mismatches.

Do not treat a build success, component-tree match, automated pixel metric, or screenshot existence alone as proof of visual alignment.
