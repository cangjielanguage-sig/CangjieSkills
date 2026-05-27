### 注入UI模拟操作

| 命令   | 必填 | 描述    |
|------|------|-----------------|
| help   | 是    | uiInput命令相关帮助信息。 |
| click   | 是    | 模拟单击操作。      |
| doubleClick   | 是    | 模拟双击操作。      |
| longClick   | 是    | 模拟长按操作。     |
| fling   | 是    | 模拟快滑操作。   |
| swipe   | 是    | 模拟慢滑操作。     |
| drag   | 是    | 模拟拖拽操作。     |
| dircFling   | 是    | 模拟指定方向滑动操作。     |
| inputText   | 是    | 模拟输入框输入文本操作。     |
| keyEvent   | 是    | 模拟实体按键事件（如：键盘，电源键，返回上一级，返回桌面等），以及组合按键操作。     |

#### uiInput click/doubleClick/longClick使用示例

| 配置参数    | 必填 | 描述   |
|---------|------|-----------------|
| point_x | 是      | 点击x坐标点。 |
| point_y | 是       | 点击y坐标点。 |

```shell
# 执行单击事件。
hdc shell uitest uiInput click 100 100

# 执行双击事件。
hdc shell uitest uiInput doubleClick 100 100

# 执行长按事件。
hdc shell uitest uiInput longClick 100 100
```

#### uiInput fling使用示例

| 配置参数  | 必填   | 描述      |
|------|------------------|-----------------|
| from_x   | 是  | 滑动起点x坐标。 |
| from_y   | 是    | 滑动起点y坐标。 |
| to_x   | 是   | 滑动终点x坐标。 |
| to_y   | 是   | 滑动终点y坐标。 |
| swipeVelocityPps_   | 否      | 滑动速度，单位：px/s，取值范围：200-40000。<br> 默认值：600。 |
| stepLength_   | 否 | 滑动步长。默认值：滑动距离/50。<br>  **为实现更好的模拟效果，推荐参数缺省/使用默认值。**  |

```shell
# 执行快滑操作，stepLength_缺省。
hdc shell uitest uiInput fling 10 10 200 200 500
```

#### uiInput swipe/drag使用示例

| 配置参数  | 必填             | 描述               |
|------|------------------|-----------------|
| from_x   | 是     | 滑动起点x坐标。 |
| from_y   | 是    | 滑动起点y坐标。 |
| to_x   | 是    | 滑动终点x坐标。 |
| to_y   | 是    | 滑动终点y坐标。 |
| swipeVelocityPps_   | 否      | 滑动速度，单位：px/s，取值范围：200-40000。<br> 默认值: 600。 |

```shell
# 执行慢滑操作。
hdc shell uitest uiInput swipe 10 10 200 200 500

# 执行拖拽操作。
hdc shell uitest uiInput drag 10 10 100 100 500
```

#### uiInput dircFling使用示例

| 配置参数  | 必填  | 描述 |
|------------|-------------|----------|
| direction  | 否 | 滑动方向，取值范围：[0,1,2,3]，默认值为0。<br> 0代表向左滑动，1代表向右滑动，2代表向上滑动，3代表向下滑动。    |
| swipeVelocityPps_ | 否| 滑动速度，单位：px/s，取值范围：200-40000。<br> 默认值: 600。    |
| stepLength   | 否   | 滑动步长。<br> 默认值: 滑动距离/50。为更好的模拟效果，推荐参数缺省/使用默认值。 |

```shell
# 执行左滑操作。
hdc shell uitest uiInput dircFling 0 500
# 执行向右滑动操作。
hdc shell uitest uiInput dircFling 1 600
# 执行向上滑动操作。
hdc shell uitest uiInput dircFling 2
# 执行向下滑动操作。
hdc shell uitest uiInput dircFling 3
```

#### uiInput inputText使用示例

| 配置参数  | 必填   | 描述 |
|------|---------|----------|
| point_x   | 是 | 输入框x坐标点。 |
| point_y   | 是   | 输入框y坐标点。 |
| text   | 是   | 输入文本内容。  |

```shell
# 执行输入框输入操作。
hdc shell uitest uiInput inputText 100 100 hello
```

#### uiInput keyEvent使用示例

| 配置参数   | 必填  | 描述 |
|------|------|----------|
| keyID1   | 是    | 实体按键对应ID，取值范围：KeyCode/Back/Home/Power。<br>当取Back/Home/Power时，不支持输入组合键。 |
| keyID2    | 否    | 实体按键对应ID。 |
| keyID3    | 否    | 实体按键对应ID。 |

> **说明：**
>
> 最多支持传入是三个键值，键值的具体取值请参考[KeyCode](../../API_Reference/source_zh_cn/apis/InputKit/cj-apis-multimodalInput-keyCode.md#enum-keycode)。

```shell
# 返回主页。
hdc shell uitest uiInput keyEvent Home
# 返回。
hdc shell uitest uiInput keyEvent Back
# 组合键粘贴。
hdc shell uitest uiInput keyEvent 2072 2038
```