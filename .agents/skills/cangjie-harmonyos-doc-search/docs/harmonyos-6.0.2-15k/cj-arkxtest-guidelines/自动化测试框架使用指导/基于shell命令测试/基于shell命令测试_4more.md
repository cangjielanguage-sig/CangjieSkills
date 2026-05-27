## 基于shell命令测试

在开发过程中，若需要快速进行截屏、录屏、注入UI模拟操作、获取控件树等操作，可以使用shell命令，更方便完成相应测试。

> **说明：**
>
> 使用cmd的方式，需要配置好hdc相关的环境变量。

**命令列表**

| 命令  | 配置参数   |描述      |
|-------|-------------|-------|
| help   | help|  显示uitest工具能够支持的命令信息。  |
| screenCap       |[-p] | 截屏。非必填。<br>指定存储路径和文件名，只支持存放在/data/local/tmp/下。<br>默认存储路径：/data/local/tmp，文件名：时间戳 + .png。 |
| dumpLayout      |[-p] \<-i \| -a>|支持在daemon运行时执行获取控件树。<br> **-p** ：指定存储路径和文件名，只支持存放在/data/local/tmp/下。默认存储路径：/data/local/tmp，文件名：时间戳 + .json。<br> **-i** ：不过滤不可见控件，也不做窗口合并。<br> **-a** ：保存 BackgroundColor、 Content、FontColor、FontSize、extraAttrs 属性数据。<br> **默认** ：不保存上述属性数据。<br> **-a和-i** 不可同时使用。 |
| uiRecord        | uiRecord \<record \| read>|录制Ui操作。  <br> **record** ：开始录制，将当前界面操作记录到/data/local/tmp/record.csv，结束录制操作使用Ctrl+C结束录制。  <br> **read** ：读取并且打印录制数据。<br>各参数代表的含义请参考[用户录制操作](#用户录制操作)。|
| uiInput| \<help \| click \| doubleClick \| longClick \| fling \| swipe \| drag \| dircFling \| inputText \| keyEvent>| 注入UI模拟操作。<br>各参数代表的含义请参考[注入ui模拟操作](#注入ui模拟操作)。   |
| --version | --version|获取当前工具版本信息。   |
| start-daemon|start-daemon| 拉起uitest测试进程。 |

### 截图使用示例

```bash
# 存储路径：/data/local/tmp，文件名：时间戳 + .png。
hdc shell uitest screenCap
# 指定存储路径和文件名，存放在/data/local/tmp/下。
hdc shell uitest screenCap -p /data/local/tmp/1.png
```

### 获取控件树使用示例

```bash
hdc shell uitest dumpLayout -p /data/local/tmp/1.json
```

### 用户录制操作

> **说明：**
>
> 录制过程中，需等待当前操作的识别结果在命令行输出后，再进行下一步操作。

```bash
# 将当前界面操作记录到/data/local/tmp/record.csv，结束录制操作使用Ctrl+C结束录制。
hdc shell uitest uiRecord record
# 读取并打印录制数据。
hdc shell uitest uiRecord read
```

以下举例为：record数据中包含的字段及字段含义，仅供参考。

```text
{
  "ABILITY": "com.ohos.launcher.MainAbility", // 前台应用界面
  "BUNDLE": "com.ohos.launcher", // 操作应用
  "CENTER_X": "", // 预留字段,暂未使用
  "CENTER_Y": "", // 预留字段,暂未使用
  "EVENT_TYPE": "pointer", //  
  "LENGTH": "0", // 总体步长
  "OP_TYPE": "click", //事件类型，当前支持点击、双击、长按、拖拽、滑动、抛滑动作录制
  "VELO": "0.000000", // 离手速度
  "direction.X": "0.000000",// 总体移动X方向
  "direction.Y": "0.000000", // 总体移动Y方向
  "duration": 33885000.0, // 手势操作持续时间
  "fingerList": [{
    "LENGTH": "0", // 总体步长
    "MAX_VEL": "40000", // 最大速度
    "VELO": "0.000000", // 离手速度
    "W1_BOUNDS": "{"bottom":361,"left":37,"right":118,"top":280}", // 起点控件bounds
    "W1_HIER": "ROOT,3,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0", // 起点控件hierarchy
    "W1_ID": "", // 起点控件id
    "W1_Text": "", // 起点控件text
    "W1_Type": "Image", // 起点控件类型
    "W2_BOUNDS": "{"bottom":361,"left":37,"right":118,"top":280}", // 终点控件bounds
    "W2_HIER": "ROOT,3,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0", // 终点控件hierarchy
    "W2_ID": "", // 终点控件id
    "W2_Text": "", // 终点控件text
    "W2_Type": "Image", // 终点控件类型
    "X2_POSI": "47", // 终点X
    "X_POSI": "47", // 起点X
    "Y2_POSI": "301", // 终点Y
    "Y_POSI": "301", // 起点Y
    "direction.X": "0.000000", // x方向移动量
    "direction.Y": "0.000000" // Y方向移动量
  }],
  "fingerNumber": "1" //手指数量
}
```