### func listDirection(?Axis)

```cangjie
public func listDirection(value: ?Axis): This
```

**功能：** 设置列表项排列的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Axis](./cj-common-types.md#enum-axis)|是|-|列表项排列方向。初始值：Axis.Vertical。|

### func multiSelectable(?Bool)

```cangjie
public func multiSelectable(value: ?Bool): This
```

**功能：** 设置是否启用多选。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否启用多选。初始值：false。|

### func sticky(?StickyStyle)

```cangjie
public func sticky(value: ?StickyStyle): This
```

**功能：** 设置是否将ListItemGroup中的header固定在顶部或将footer固定在底部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[StickyStyle](./cj-common-types.md#enum-stickystyle)|是|-|粘性样式。初始值：StickyStyle.None。|