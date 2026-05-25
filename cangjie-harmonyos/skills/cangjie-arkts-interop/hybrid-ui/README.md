# 混合 UI 与跨语言路由

## 核心规则

1. 仓颉页面**不是完整页面**，只能以**组件**形式嵌入 ArkTS `@Entry` 容器页
2. 每个仓颉"页面"必须成对出现：`xxx.cj`（仓颉组件）+ `xxx.ets`（ArkTS 容器）
3. 仓颉组件**无法直接使用** ArkTS 的 `router`，跨语言路由必须走回调桥
4. 架构层次：`ArkTS @Entry 页面` → `CJHybridComponent` → `仓颉 @Component`

## CJHybridComponent 嵌入

ArkTS 容器页通过 `CJHybridComponent` 加载仓颉组件：

```typescript
import { CJHybridComponent } from '@cangjie/cjhybridcomponent';
@Entry @Component struct XxxPage {
  build() {
    Row() {
      CJHybridComponent({
        library: "ohos_app_cangjie_entry",
        component: "Xxx"
      })
    }.height('100%').width('100%')
  }
}
```

仓颉组件必须使用 `@HybridComponentEntry` + `@Component` 注解。

**参数对齐要求：**

| 参数 | 必须等于 |
|------|---------|
| `library` | `cjpm.toml` 的 `package name` |
| `component` | 仓颉 `@Component class` 名 |

容器页路径必须在 `main_pages.json` 的 `src` 数组中注册。

## 跨语言页面路由桥接

仓颉与 ArkTS 的 `router` **不互通**。标准做法：用全局 HashMap 存 ArkTS 回调，通过 `@Interop` 暴露注册/注销函数。

**仓颉侧（index.cj）** 提供注册中心：

```cangjie
public let globalJSFunction = HashMap<String, ()->Unit>()

@Interop[ArkTS]
public func registerJSFunc(name: String, fn: ()->Unit): Unit {
    if (globalJSFunction.contains(name)) { return }
    globalJSFunction.add(name, fn)
}

@Interop[ArkTS]
public func unregisterJSFunc(name: String): Unit {
    globalJSFunction.remove(name)
}
```

**ArkTS 侧**在容器页生命周期中注册/注销回调：
- `aboutToAppear`：注册回调（如 `router.back()`）
- `aboutToDisappear`：注销回调，防止泄漏

**仓颉侧**按名取回调并调用：
- `globalJSFunction.get("key")` → `if (let Some(fn) <- optFn) { fn() }`

**路由桥接规则：**
- 回调命名建议 `{PageName}{Action}`，如 `SecondPageRouterBack`
- ArkTS→ArkTS 直接 `router.pushUrl`；仓颉→ArkTS 必须走回调桥
- 同一模式可扩展到弹窗、权限申请等任意 ArkTS 能力

## 关键目录与配置文件

```
entry/src/main/
├── cangjie/                ← 仓颉源码 + index.cj（互操作入口）
│    └── types/             ← Generate 产物（Index.d.ts）
├── ets/pages/              ← ArkTS 容器页
└── resources/base/profile/main_pages.json ← 路由表
```

| 文件 | 职责 |
|------|------|
| `cjpm.toml` | 仓颉包名、编译选项、依赖 |
| `oh-package.json5` | 须含 `libohos_app_cangjie_entry.so` + `@cangjie/cjhybridcomponent` |
| `build-profile.json5` | 构建配置，含 `cangjieOptions` / `abiFilters` |
| `main_pages.json` | 页面路由注册表 |

## 新增仓颉混合页面步骤

1. 右键 `cangjie` 文件夹 → **New → Cangjie HybridComponent File**
2. 填写 Component name，Language 选 **Cangjie**，Type 选 **With ArkTS Wrapper**
3. 自动生成 `xxx.cj`（仓颉组件）+ `pages/xxx.ets`（ArkTS 容器）
4. 确认 `main_pages.json` 已自动添加 `pages/xxx` 路由
5. 如需路由交互，在 `index.cj` 用 `@Interop` 注册回调桥函数，重新 Generate

## 模拟器 abiFilters 配置

仓颉默认编译 `arm64-v8a`。使用 x86 模拟器时须在 `entry/build-profile.json5` 增加 `x86_64`：

```json
"cangjieOptions": { "abiFilters": ["arm64-v8a", "x86_64"] }
```

## 注意事项

1. `library` / `component` 参数与仓颉包名 / class 名不一致会导致组件不显示
2. 容器页路径未在 `main_pages.json` 注册会导致路由跳转失败
3. 仓颉侧不能直接调用 ArkTS `router`，必须通过回调桥
4. `oh-package.json5` 缺少 `.so` 依赖会导致 ArkTS 找不到互操作接口
5. x86 模拟器缺 `x86_64` abiFilter 会导致运行崩溃
6. 回调注册时机必须早于仓颉组件 `build`，否则回调未触发
7. 必须在 `aboutToDisappear` 中 `unregisterJSFunc`，否则回调泄漏
