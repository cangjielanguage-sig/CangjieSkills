# 进度条（Progress）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参见[Progress](../reference/arkui-cj/cj-information-display-progress.md)。

## 创建进度条

Progress通过调用接口来创建，接口调用形式如下：

```cangjie
Progress(value!: Float64, total!: Float64 = 100.0, progressType!: ProgressType = ProgressType.Linear)
```

其中，value用于设置初始进度值，total用于设置进度总长度，ProgressType用于设置ProgressType样式。

<!-- code_check_manual -->

```cangjie
Progress(value: 24.0, total: 100.0, progressType: ProgressType.Linear) // 创建一个进度总长为100，初始进度值为24的线性进度条
```

![create](figures/create.png)