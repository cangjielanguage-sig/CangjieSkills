# CJHybridComponent UI Embedding

Use this reference when an ArkTS page embeds a Cangjie component.

## Shape

ArkTS page:

```typescript
import { CJHybridComponent } from '@cangjie/cjhybridcomponent';

@Entry
@Component
struct Index {
  build() {
    Row() {
      CJHybridComponent({
        library: 'ohos_app_cangjie_entry',
        component: 'EntryView'
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

Cangjie component:

```cangjie
@HybridComponentEntry
@Component
class EntryView {
    func build() {
        Text("Hello Hybrid")
    }
}
```

## Tooling

Create a wrapper page from the project root:

```powershell
python -B <cangjie-arkts-interop-skill>/tools/add_hybrid_component.py --component MetricsPanel --page metrics --title "Cangjie Metrics"
```

Then route to `pages/metrics` from ArkTS or embed `CJHybridComponent` directly in an existing ArkTS page.

For API 18 and later, route from an ArkUI component through its `UIContext` without importing the deprecated global router object:

```typescript
Button('Open metrics')
  .onClick(() => {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/metrics' });
  });

Button('Back')
  .onClick(() => {
    this.getUIContext().getRouter().back();
  });
```

## Alignment Rules

- `library` equals `cjpm.toml` `[package].name`, not the `lib*.so` import string.
- `component` equals the Cangjie component class name.
- The ArkTS wrapper page must be listed in `main_pages.json`.
- Use ArkTS for router/page lifecycle and Cangjie for embedded component UI.
- If Cangjie needs ArkTS router behavior, pass callbacks through an interop boundary instead of calling ArkTS router directly.
- Add `@cangjie/cjhybridcomponent` to `entry/oh-package.json5` only for mixed UI component use. The packaged generator currently pins the tested `1.1.1` release rather than silently following `latest`.
- The Cangjie component appears in the UI tree under an ArkTS common/native container such as `__Common__`; assert business text inside it, not only the wrapper page.

## Build and Runtime Notes

- Package-owned warnings must be distinguished from application-source warnings. The generator uses `@cangjie/cjhybridcomponent` 1.1.1 to avoid known 1.0.0 migration noise; if the current upstream package still emits a lint or resource conflict warning, report the exact package path and warning after a successful build/runtime assertion instead of suppressing or relabeling it as application code.
- A Cangjie hybrid component is not a full Cangjie page. It has no independent page lifecycle and does not own ArkTS router behavior.
- Prefer an ArkTS wrapper page for routing. Inline embedding into an existing ArkTS page is also valid when the layout is simple.
