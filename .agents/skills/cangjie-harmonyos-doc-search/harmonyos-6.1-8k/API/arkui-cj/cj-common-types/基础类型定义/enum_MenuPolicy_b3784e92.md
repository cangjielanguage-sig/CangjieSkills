## enum MenuPolicy

```cangjie
public enum MenuPolicy <: Equatable<MenuPolicy> {
    | Default
    | Hide
    | Show
    | ...
}
```

**功能：** 菜单弹出的策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[MenuPolicy](#enum-menupolicy)>

### Default

```cangjie
Default
```

**功能：** 按照底层默认逻辑决定是否弹出菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Hide

```cangjie
Hide
```

**功能：** 始终不弹出菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Show

```cangjie
Show
```

**功能：** 始终弹出菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(MenuPolicy)

```cangjie
public operator func ==(other: MenuPolicy): Bool
```

**功能：** 判断两个MenuPolicy枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MenuPolicy](#enum-menupolicy)|是|-|要比较的另一个MenuPolicy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(MenuPolicy)

```cangjie
public operator func !=(other: MenuPolicy): Bool
```

**功能：** 判断两个MenuPolicy枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MenuPolicy](#enum-menupolicy)|是|-|要比较的另一个MenuPolicy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|