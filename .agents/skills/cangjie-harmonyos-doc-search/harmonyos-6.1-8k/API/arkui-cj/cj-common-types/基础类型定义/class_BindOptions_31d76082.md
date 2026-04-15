## class BindOptions

```cangjie
public open class BindOptions {
    public init(backgroundColor!: ?ResourceColor = None, onAppear!: ?() -> Unit = None, onDisappear!: ?() -> Unit = None, onWillAppear!: ?() -> Unit = None, onWillDisappear!: ?() -> Unit = None)
}
```

**功能：** 配置半模态页面的可选属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ResourceColor, ?() -> Unit, ?() -> Unit, ?() -> Unit, ?() -> Unit)

```cangjie
public init(backgroundColor!: ?ResourceColor = None, onAppear!: ?() -> Unit = None, onDisappear!: ?() -> Unit = None, onWillAppear!: ?() -> Unit = None, onWillDisappear!: ?() -> Unit = None)
```

**功能：** 配置半模态页面的可选属性构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 半模态页面的背板颜色。默认值：**Color.White**。|
|onAppear|?() -> Unit|否|None|**命名参数。** 半模态页面显示（动画结束后）回调函数。|
|onDisappear|?() -> Unit|否|None|**命名参数。** 半模态页面回退（动画结束后）回调函数。|
|onWillAppear|?() -> Unit|否|None|**命名参数。** 半模态页面显示（动画开始前）回调函数。|
|onWillDisappear|?() -> Unit|否|None|**命名参数。** 半模态页面回退（动画开始前）回调函数。<br>**说明：** 不允许在onWillDisappear函数中修改状态变量，可能会导致组件行为不稳定。|