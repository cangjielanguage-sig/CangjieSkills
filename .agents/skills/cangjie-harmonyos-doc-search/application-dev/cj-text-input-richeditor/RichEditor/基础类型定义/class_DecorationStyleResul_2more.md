### class DecorationStyleResult

```cangjie
public class DecorationStyleResult {
    public var decorationType: ?TextDecorationType
    public var color: ResourceColor
    public init(
        decorationType: TextDecorationType,
        color: ResourceColor
    )
}
```

**功能：** 定义装饰样式结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var decorationType

```cangjie
public var decorationType: ?TextDecorationType
```

**功能：** 装饰类型。

**类型：** ?[TextDecorationType](./cj-common-types.md#enum-textdecorationstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var color

```cangjie
public var color: ResourceColor
```

**功能：** 颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(TextDecorationType, ResourceColor)

```cangjie
public init(
    decorationType: TextDecorationType,
    color: ResourceColor
)
```

**功能：** DecorationStyleResult构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|decorationType|[TextDecorationType](./cj-common-types.md#enum-textdecorationstyle)|是|-|装饰类型。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|颜色。|

### class SelectionMenuOptions

```cangjie
public class SelectionMenuOptions {
    public var onAppear: ?VoidCallback
    public var onDisappear: ?VoidCallback
    public init(onAppear!: ?() -> Unit = None, onDisappear!: ?() -> Unit = None)
}
```

**功能：** 定义选择菜单选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var onAppear

```cangjie
public var onAppear: ?VoidCallback
```

**功能：** 选择菜单出现时的回调函数。

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var onDisappear

```cangjie
public var onDisappear: ?VoidCallback
```

**功能：** 选择菜单消失时的回调函数。

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?() -> Unit, ?() -> Unit)

```cangjie
public init(onAppear!: ?() -> Unit = None, onDisappear!: ?() -> Unit = None)
```

**功能：** SelectionMenuOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onAppear|?() -> Unit|否|None|**命名参数。** 选择菜单出现时的回调函数。初始值：{=>}。|
|onDisappear|?() -> Unit|否|None|**命名参数。** 选择菜单消失时的回调函数。初始值：{=>}。|