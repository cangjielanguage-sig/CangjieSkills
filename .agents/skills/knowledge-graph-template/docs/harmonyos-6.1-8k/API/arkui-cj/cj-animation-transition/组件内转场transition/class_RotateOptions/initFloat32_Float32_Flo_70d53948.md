### init(?Float32, ?Float32, ?Float32, ?Float32, ?Length, ?Length, ?Length, ?Float32)

```cangjie
public init(angle: ?Float32, x!: ?Float32 = None, y!: ?Float32 = None, z!: ?Float32 = None, centerX!: ?Length = None,
        centerY!: ?Length = None, centerZ!: ?Length = None, perspective!: ?Float32 = None)
```

**功能：** RotateOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|?Float32|是|-|角度参数。|
|x|?Float32|否|None|**命名参数。** 旋转轴向量的X坐标。<br>初始值：0.0。|
|y|?Float32|否|None|**命名参数。** 旋转轴向量的Y坐标。<br>初始值：0.0。|
|z|?Float32|否|None|**命名参数。** 旋转轴向量的Z坐标。<br>初始值：0.0。|
|centerX|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 变换中心点（锚点）的X坐标。<br>对于数字类型，单位为vp。<br>初始值：50.percent。|
|centerY|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 变换中心点（锚点）的Y坐标。<br>对于数字类型，单位为vp。<br>初始值：50.percent。|
|centerZ|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** Z轴锚点，即3D旋转中心点的z分量。<br>对于数字类型，单位为vp。<br>初始值：0。|
|perspective|?Float32|否|None|**命名参数。** 用户到z=0平面的距离。轴和旋转中心是基于坐标系设置的，当组件移动时坐标系保持不变。<br>初始值：0.0。<br>单位：px。|