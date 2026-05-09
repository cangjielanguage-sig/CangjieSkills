# Knowledge Graph Report

**Nodes:** 20468
**Edges:** 32450
**Communities:** 1148

## God Nodes (Most Connected)

These nodes are the core abstractions of the knowledge graph:

1. `cangjie code` - 3194 edges
2. `text code` - 468 edges
3. `core_package_structs.md#struct-string` - 357 edges
4. `core_package_intrinsics.md#int64` - 352 edges
5. `core_package_intrinsics.md#bool` - 336 edges
6. `core_package_exceptions.md#class-illegalargumentexception` - 268 edges
7. `core_package_structs.md#struct-arrayt` - 207 edges
8. `init()` - 183 edges
9. `cj-errorcode-universal.md` - 150 edges
10. `core_package_enums.md#enum-optiont` - 130 edges

## Surprising Connections

Cross-community edges that bridge distant parts of the graph:

- `cj-apis-ability-ability_result.md` ↔ `cj-apis-app-ability-want.md#class-want` - references [EXTRACTED]
  - bridges separate communities
- `cj-apis-app-ability-ui_ability.md#class-context` ↔ `cj-apis-common_event_data.md` - references [EXTRACTED]
  - bridges separate communities
- `cj-development-intro.md#仓颉示例代码说明` ↔ `cj-apis-common_event_data.md` - references [EXTRACTED]
  - bridges separate communities
- `cj-apis-app-ability-want.md#class-want` ↔ `cj-apis-app-ability-dialog_request.md` - references [EXTRACTED]
  - bridges separate communities
- `cj-apis-syscap.md` ↔ `cangjie code` - contains_code [EXTRACTED]
  - bridges separate communities

## Communities

- **Community 0** (2585 nodes, cohesion: 0.0)
- **Community 1** (2026 nodes, cohesion: 0.0)
- **Community 2** (1062 nodes, cohesion: 0.0)
- **Community 3** (916 nodes, cohesion: 0.0)
- **Community 4** (853 nodes, cohesion: 0.0)
- **Community 5** (788 nodes, cohesion: 0.0)
- **Community 6** (617 nodes, cohesion: 0.0)
- **Community 7** (548 nodes, cohesion: 0.01)
- **Community 8** (538 nodes, cohesion: 0.01)
- **Community 9** (499 nodes, cohesion: 0.0)

## Suggested Questions

- Why does `cangjie code` bridge different communities?
  - High betweenness centrality (0.735)
- Why does `cj-errorcode-universal.md` bridge different communities?
  - High betweenness centrality (0.061)
- Why does `cj-errorcode-data-rdb.md` bridge different communities?
  - High betweenness centrality (0.021)
- What connects `ohos.ability.ability_result`, `class AbilityResult`, `var resultCode` to the rest?
  - 12970 weakly-connected nodes
- Should `Community 14` be split into smaller modules?
  - Cohesion score 0.01
- Should `Community 13` be split into smaller modules?
  - Cohesion score 0.01
- Should `Community 1` be split into smaller modules?
  - Cohesion score 0.0
