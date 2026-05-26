### class LocalizedEdgeWidths

```cangjie
public class LocalizedEdgeWidths {
    public var bottom: Option<Length>
    public var end: Option<Length>
    public var start: Option<Length>
    public var top: Option<Length>
    public init(
        bottom!: Option<Length> = Option.None,
        end!: Option<Length> = Option.None,
        start!: Option<Length> = Option.None,
        top!: Option<Length> = Option.None
    )
}
```

**功能：** 边框宽度类型，用于描述组件边框不同方向的宽度。引入该对象时，至少传入一个参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var bottom

```cangjie
public var bottom: Option<Length>
```

**功能：** 下侧边框宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var end

```cangjie
public var end: Option<Length>
```

**功能：** 右侧边框宽度。从右至左显示语言模式下为左侧边框宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var start

```cangjie
public var start: Option<Length>
```

**功能：** 左侧边框宽度。从右至左显示语言模式下为右侧边框宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var top

```cangjie
public var top: Option<Length>
```

**功能：** 上侧边框宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Option\<Length>, Option\<Length>, Option\<Length>, Option\<Length>)

```cangjie
public init(start!: Option<Length> = Option.None, bottom!: Option<Length> = Option.None, end!: Option<Length> = Option.None, top!: Option<Length> = Option.None)
```

**功能：** 构造一个LocalizedEdgeWidths类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :---------- | :---------- | :------- | :------ |
| start |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  左侧边框宽度。从右至左显示语言模式下为右侧边框宽度。|
| bottom |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  下侧边框宽度。|
| end |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  右侧边框宽度。从右至左显示语言模式下为左侧边框宽度。|
| top |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  上侧边框宽度。|