### class LocalizedBorderRadiuses

```cangjie
public class LocalizedBorderRadiuses {
    public var bottomEnd: Option<Length>
    public var bottomStart: Option<Length>
    public var topEnd: Option<Length>
    public var topStart: Option<Length>
    public init(
        bottomEnd!: Option<Length> = Option.None,
        bottomStart!: Option<Length> = Option.None,
        topEnd!: Option<Length> = Option.None,
        topStart!: Option<Length> = Option.None
    )
}
```

**功能：** 圆角类型，用于描述组件边框圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var bottomEnd

```cangjie
public var bottomEnd: Option<Length>
 ```

**功能：** 右下角圆角半径。从右至左显示语言模式下为左下角圆角半径。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var bottomStart

```cangjie
public var bottomStart: Option<Length>
 ```

**功能：** 左下角圆角半径。从右至左显示语言模式下为右下角圆角半径。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var topEnd

```cangjie
public var topEnd: Option<Length>
 ```

**功能：** 右上角圆角半径。从右至左显示语言模式下为左上角圆角半径。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var topStart

```cangjie
public var topStart: Option<Length>
 ```

**功能：** 左上角圆角半径。从右至左显示语言模式下为右上角圆角半径。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Option\<Length>, Option\<Length>, Option\<Length>, Option\<Length>)

```cangjie
public init(bottomEnd!: Option<Length> = Option.None, bottomStart!: Option<Length> = Option.None, topEnd!: Option<Length> = Option.None,topStart!: Option<Length> = Option.None)
```

**功能：** 构造一个LocalizedBorderRadiuses类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :---------- | :---------- | :------- | :------ |
| bottomEnd |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  右下角圆角半径。从右至左显示语言模式下为左下角圆角半径。|
| bottomStart |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  左下角圆角半径。从右至左显示语言模式下为右下角圆角半径。|
| topEnd |Option\<[Length](./cj-common-types.md#interface-length)>| 否 | Option.None| **命名参数。**  右上角圆角半径。从右至左显示语言模式下为左上角圆角半径。|
| topStart |Option\<[Length](./cj-common-types.md#interface-length)> |  否 |Option.None| 左上角圆角半径。从右至左显示语言模式下为右上角圆角半径。|