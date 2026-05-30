# 形状裁剪

用于对组件进行裁剪、遮罩处理。

## func clip(Bool)

```cangjie
public func clip(isClip: Bool): This
```

**功能：** 是否对子组件超出当前组件范围外的区域进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isClip  | Bool | 是   | - | 是否按照父容器边缘轮廓进行裁剪。<br/>初始值：false<br/>**说明：** true表示进行裁剪，false表示不进行裁剪。<br/>设置为true后，子组件超出当前组件范围外的区域将不响应绑定的手势事件。|

## func clip(CircleShape)

```cangjie
public func clip(shape: CircleShape): This
```

**功能：** 按[CircleShape](#class-circleshape)的形状对当前组件进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [CircleShape](#class-circleshape) | 是   | - | 对当前组件进行裁剪的指定的形状。|

## func clip(EllipseShape)

```cangjie
public func clip(shape: EllipseShape): This
```

**功能：** 按[EllipseShape](#class-ellipseshape)的形状对当前组件进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [EllipseShape](#class-ellipseshape) | 是   | - | 对当前组件进行裁剪的指定的形状。|

## func clip(RectShape)

```cangjie
public func clip(shape: RectShape): This
```

**功能：** 按[RectShape](#class-rectshape)的形状对当前组件进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [RectShape](#class-rectshape) | 是   | - | 对当前组件进行裁剪的指定的形状。|

## func clip(PathShape)

```cangjie
public func clip(shape: PathShape): This
```

**功能：** 按[PathShape](#class-pathshape)的形状对当前组件进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [PathShape](#class-pathshape) | 是   | - | 对当前组件进行裁剪的指定的形状。|

## func mask(CircleShape)

```cangjie
public func mask(shape: CircleShape): This
```

**功能：** 为组件上添加[CircleShape](#class-circleshape)形状的遮罩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [CircleShape](#class-circleshape) | 是   | - | 对当前组件进行遮罩指定的形状。|

## func mask(EllipseShape)

```cangjie
public func mask(shape: EllipseShape): This
```

**功能：** 为组件上添加[EllipseShape](#class-ellipseshape)形状的遮罩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [EllipseShape](#class-ellipseshape) | 是   | - | 对当前组件进行遮罩指定的形状。|

## func mask(RectShape)

```cangjie
public func mask(shape: RectShape): This
```

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**功能：** 为组件上添加[RectShape](#class-rectshape)形状的遮罩。

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [RectShape](#class-rectshape) | 是   | - | 对当前组件进行遮罩指定的形状。|

## func mask(PathShape)

```cangjie
public func mask(shape: PathShape): This
```

**功能：** 为组件上添加[PathShape](#class-pathshape)形状的遮罩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| shape  | [PathShape](#class-pathshape) | 是   | - | 对当前组件进行遮罩指定的形状。|