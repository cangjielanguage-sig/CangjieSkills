## func systemBarEffect()

```cangjie
public func systemBarEffect(): This
```

**功能：** 根据背景进行智能反色并且带有模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## func useShadowBatching(Bool)

```cangjie
public func useShadowBatching(value: Bool): This
```

**功能：** 控件内部子节点的阴影进行同层绘制，同层元素阴影重叠。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|\-|控件内部子节点的阴影进行同层绘制，同层元素阴影重叠。 <br> 初始值：false。<br>**说明：** <br> 1. 默认不开启，如果子节点的阴影半径较大，节点各自的阴影会互相重叠。 当开启时，元素的阴影将不会重叠。<br>2. 不推荐useShadowBatching嵌套使用，如果嵌套使用，只会对当前的子节点生效，无法递推。|