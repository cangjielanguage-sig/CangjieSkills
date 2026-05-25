### class RichEditorLayoutStyle

```cangjie
public class RichEditorLayoutStyle {
    public var margin: ?Margin
    public var borderRadius: ?BorderRadiuses
    public init(margin!: ?Margin = None, borderRadius!: ?BorderRadiuses = None)
    public init(margin!: ?Length, borderRadius!: ?Length)
}
```

**功能：** 定义richEditor图像布局样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var margin

```cangjie
public var margin: ?Margin
```

**功能：** 边距。

**类型：** ?[Margin](./cj-common-types.md#class-margin)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var borderRadius

```cangjie
public var borderRadius: ?BorderRadiuses
```

**功能：** 边框圆角。

**类型：** ?[BorderRadiuses](./cj-common-types.md#class-borderradiuses)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Margin, ?BorderRadiuses)

```cangjie
public init(margin!: ?Margin = None, borderRadius!: ?BorderRadiuses = None)
```

**功能：** RichEditorLayoutStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|margin|?[Margin](./cj-common-types.md#class-margin)|否|None|**命名参数。** 边距。初始值：Margin()。|
|borderRadius|?[BorderRadiuses](./cj-common-types.md#class-borderradiuses)|否|None|**命名参数。** 边框圆角。初始值：BorderRadiuses()。|

#### init(?Length, ?Length)

```cangjie
public init(margin!: ?Length, borderRadius!: ?Length)
```

**功能：** RichEditorLayoutStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|margin|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 边距。|
|borderRadius|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 边框圆角。|