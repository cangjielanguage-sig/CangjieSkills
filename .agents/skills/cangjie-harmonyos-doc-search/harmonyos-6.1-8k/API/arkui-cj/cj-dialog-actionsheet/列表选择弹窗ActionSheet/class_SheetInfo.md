## class SheetInfo

```cangjie
public class SheetInfo {
    public var title: ?ResourceStr
    public var icon: ?ResourceStr
    public var action: ?VoidCallback
    public init(
        title!: ?ResourceStr,
        icon!: ?ResourceStr = None,
        action!: ?VoidCallback
    )
}
```

**功能：** 设置选项内容，每个选择项支持设置图片、文本和选中的回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var action

```cangjie
public var action: ?VoidCallback
```

**功能：** 选项选中的回调。

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var icon

```cangjie
public var icon: ?ResourceStr
```

**功能：** 选项的图标，默认无图标显示。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var title

```cangjie
public var title: ?ResourceStr
```

**功能：** 选项的文本内容。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ResourceStr, ?ResourceStr, ?VoidCallback)

```cangjie
public init(
    title!: ?ResourceStr,
    icon!: ?ResourceStr = None,
    action!: ?VoidCallback
)
```

**功能：** SheetInfo类的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 选项的文本内容。<br/>文本超长时会触发滚动条。|
|icon|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 选项的图标，默认无图标显示。<br/>string格式可用于加载网络图片和本地图片，常用于加载网络图片。当使用相对路径引用本地图片时，例如Image("common/test.jpg")。|
|action|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|**命名参数。** 选项选中时的回调。|