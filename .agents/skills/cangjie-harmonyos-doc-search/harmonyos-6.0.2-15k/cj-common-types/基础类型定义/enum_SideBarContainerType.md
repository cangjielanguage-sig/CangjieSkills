## enum SideBarContainerType

```cangjie
public enum SideBarContainerType {
    | Embed
    | Overlay
    | AUTO
}
```

**功能：** 容器内侧边栏样式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### AUTO

```cangjie
AUTO
```

**功能：** 组件尺寸大于等于[minSideBarWidth](./cj-grid-layout-sidebar.md#func-minsidebarwidthlength)+[minContentWidth](./cj-grid-layout-sidebar.md#func-mincontentwidthlength)时，采用Embed模式显示。

组件尺寸小于[minSideBarWidth](./cj-grid-layout-sidebar.md#func-minsidebarwidthlength)+[minContentWidth](./cj-grid-layout-sidebar.md#func-mincontentwidthlength)时，采用Overlay模式显示。contagrid

未设置[minSideBarWidth](./cj-grid-layout-sidebar.md#func-minsidebarwidthlength)或[minContentWidth](./cj-grid-layout-sidebar.md#func-mincontentwidthlength)时，会使用未设置接口的默认值进行计算，若计算的值小于600vp，则使用600vp做为模式切换的断点值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Embed

```cangjie
Embed
```

**功能：** 侧边栏嵌入到组件内，和内容区并列显示。

组件尺寸小于[minSideBarWidth](./cj-grid-layout-sidebar.md#func-minsidebarwidthlength)+[minContentWidth](./cj-grid-layout-sidebar.md#func-mincontentwidthlength),并且未设置[showSideBar](./cj-grid-layout-sidebar.md#func-showsidebarbool)时，侧边栏自动隐藏。

未设置[minSideBarWidth](./cj-grid-layout-sidebar.md#func-minsidebarwidthlength)或[minContentWidth](./cj-grid-layout-sidebar.md#func-mincontentwidthlength)采用未设置接口的默认值进行计算。

组件在自动隐藏后，如果通过点击控制按钮唤出侧边栏，则侧边栏悬浮在内容区上显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Overlay

```cangjie
Overlay
```

**功能：** 侧边栏浮在内容区上面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12