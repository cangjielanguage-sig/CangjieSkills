## enum Mode

```cangjie
public enum Mode <: Equatable<Mode> & ToString{
    | Background
    | Foreground
    | ...
}
```

**功能：** 定义模式选项。

当应用的前台任务切换到后台一段时间后会显示运行失败或暂停，而后台任务不受此操作影响。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**父类型：**

- Equatable\<Mode>
- ToString

### Background

```cangjie
Background
```

**功能：** 表示后台任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Foreground

```cangjie
Foreground
```

**功能：** 表示前端任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func !=(Mode)

```cangjie
public operator func !=(other: Mode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型               | 必填 | 默认值 | 说明     |
| :----- | :----------------- | :--- | :----- | :------- |
| other  | [Mode](#enum-mode) | 是   | -      | 另一个模式选项。 |

**返回值：**

| 类型 | 说明                                      |
| :--- | :---------------------------------------- |
| Bool | 两个枚举值不相等返回true，否则返回false。 |

### func ==(Mode)

```cangjie
public operator func ==(other: Mode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型               | 必填 | 默认值 | 说明     |
| :----- | :----------------- | :--- | :----- | :------- |
| other  | [Mode](#enum-mode) | 是   | -      | 另一个模式选项。 |

**返回值：**

| 类型 | 说明                                    |
| :--- | :-------------------------------------- |
| Bool | 两个枚举值相等返回true，否则返回false。 |

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型   | 说明                       |
| :----- | :------------------------- |
| String | 当前枚举的字符串表示。 |