## func borderRadius(Length, Length, Length, Length)

```cangjie
public func borderRadius(topLeft!: Length = 0.vp, topRight!: Length = 0.vp, bottomLeft!: Length = 0.vp, bottomRight!: Length = 0.vp): This
```

**功能：** 设置边框的圆角。圆角大小受组件尺寸限制，最大值为组件宽或高的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :---------- | :---------- | :------- | :-------- | :---------|
| topLeft | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  左上角圆角半径。|
| topRight | [Length](./cj-common-types.md#interface-length) | 否  | 0.vp | **命名参数。**  右上角圆角半径。|
| bottomLeft | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  左下角圆角半径。|
| bottomRight | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  右下角圆角半径。|