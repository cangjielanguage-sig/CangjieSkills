## enum IndexerAlign

```cangjie
public enum IndexerAlign <: Equatable<IndexerAlign> {
    | Left
    | Right
    | ...
}
```

**功能：** 索引器对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[IndexerAlign](#enum-indexeralign)>

### Left

```cangjie
Left
```

**功能：** 左对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 右对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(IndexerAlign)

```cangjie
public operator func ==(other: IndexerAlign): Bool
```

**功能：** 判断两个IndexerAlign枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[IndexerAlign](#enum-indexeralign)|是|-|要比较的另一个IndexerAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(IndexerAlign)

```cangjie
public operator func !=(other: IndexerAlign): Bool
```

**功能：** 判断两个IndexerAlign枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[IndexerAlign](#enum-indexeralign)|是|-|要比较的另一个IndexerAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|