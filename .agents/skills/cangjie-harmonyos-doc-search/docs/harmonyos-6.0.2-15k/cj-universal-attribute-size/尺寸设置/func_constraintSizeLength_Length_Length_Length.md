## func constraintSize(Length, Length, Length, Length)

```cangjie
public func constraintSize(minWidth!: Length = 0.vp, maxWidth!: Length = (Float64.Inf).vp, minHeight!: Length = 0.vp, maxHeight!: Length = (Float64.Inf).vp): This
```

**功能：** 设置约束尺寸，组件布局时，进行尺寸范围限制。

> **说明：**
>
> Width和Height。取值结果参考constraintSize取值对width/height影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| minWidth | [Length](./cj-common-types.md#interface-length)  | 否  | 0.vp | **命名参数。**  元素最小宽度。</br>初始值：0.vp。|
| maxWidth | [Length](./cj-common-types.md#interface-length)  | 否  | (Float64.Inf).vp| **命名参数。**  元素最大宽度。</br>初始值：(Float64.Inf).vp。|
| minHeight | [Length](./cj-common-types.md#interface-length)  | 否  |0.vp | **命名参数。**  元素最小高度。</br>初始值：0.vp。|
| maxHeight | [Length](./cj-common-types.md#interface-length)  | 否  | (Float64.Inf).vp| **命名参数。**  元素最大高度。</br>初始值：(Float64.Inf).vp。|

**constraintSize(minWidth/maxWidth/minHeight/maxHeight)取值对width/height影响**

| 缺省值 | 结果  |
| :------ | :------ |
| \ | width=MAX(minWidth,MIN(maxWidth,width))<br/>height=MAX(minHeight,MIN(maxHeight,height)) |
| maxWidth、maxHeight | **命名参数。**  width=MAX(minWidth,width)<br/>height=MAX(minHeight,height) |
| minWidth、minHeight | **命名参数。**  width=MIN(maxWidth,width)<br/>height=MIN(maxHeight,height) |
| width、height | 若minWidth<maxWidth，组件自身布局逻辑生效，width取值范围为[minWidth,maxWidth]；否则，width=MAX(minWidth,maxWidth)。<br/>若minHeight<maxHeight，组件自身布局逻辑生效，height取值范围为[minHeight,maxHeight]；否则，height=MAX(minHeight,maxHeight)。 |
| width与maxWidth、height与maxHeight | width=minWidth<br/>height=minHeight |
| width与minWidth、height与minHeight | 组件自身布局逻辑生效，width取值约束为不大于maxWidth。<br/>组件自身布局逻辑生效，height取值约束为不大于maxHeight。 |
| minWidth与maxWidth、minHeight与maxHeight | **命名参数。**  width以所设值为基础，根据其他布局属性发生可能的拉伸或者压缩。<br/>height以所设值为基础，根据其他布局属性发生可能的拉伸或者压缩。|
| width与minWidth与maxWidth | 使用父容器传递的布局限制进行布局。 |
| height与minHeight与maxHeight | 使用父容器传递的布局限制进行布局。 |