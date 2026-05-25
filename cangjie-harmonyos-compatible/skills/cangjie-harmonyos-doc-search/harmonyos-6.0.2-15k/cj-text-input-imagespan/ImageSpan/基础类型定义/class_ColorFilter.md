### class ColorFilter

```cangjie
public class ColorFilter {
    public init(array: Array<Float32>)
}
```

**功能：** 表示4*5矩阵颜色过滤器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Array\<Float32>)

```cangjie
public init(array: Array<Float32>)
```

**功能：** 创建ColorFilter类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 类型 | 必填   | 默认值  | 说明 |
|:------|:------|:-----|:----|:-----------|
| array | Array\<Float32> | 是  | -   | 创建具有4\*5矩阵的颜色过滤器，入参为[m*n]位于m行和n列中矩阵值，矩阵是行优先的。|