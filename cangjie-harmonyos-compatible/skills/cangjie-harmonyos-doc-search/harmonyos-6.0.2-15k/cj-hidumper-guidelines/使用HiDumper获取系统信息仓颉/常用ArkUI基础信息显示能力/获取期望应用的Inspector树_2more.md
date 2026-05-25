### 获取期望应用的Inspector树

上述示例中的element/render树主要包含多项内部实现，与应用代码中的组件无法一一对应。可以通过打印Inspector树来获取与应用中组件对应的树结构及组件基本信息。Inspector树与DevEco Testing及DevEco中的ArkUI Inspector完全匹配。

使用此功能需要先打开ArkUI debug调试开关。

```shell
hdc shell param set persist.ace.testmode.enabled 1
```

set: 设置命令；persist.ace.testmode.enabled：ArkUI debug调试开关名称；1：开关设置为true，打开调试功能。

命令如下：

```shell
hdc shell "hidumper -s WindowManagerService -a '-w %windowId% -inspector'"
```

**使用样例：**

```text
hdc shell "hidumper -s WindowManagerService -a '-w 5 -inspector'"

|-> rootstacktag childSize:1
| ID: 2100001
| compid:
| text:
| top: 72.000000
| left: 0.000000
| width: 0.000000
| height: 0.000000
| visible: 1
| clickable: 0
| checkable: 0
|-> Column childSize:1
| ID: 128
| compid:
| text:
| top: 72.000000
| left: 0.000000
| width: 720.000000
| height: 1136.000000
| visible: 1
| clickable: 0
| checkable: 0
|-> GridContainer childSize:1
| ID: 129
| compid:
| text:
| top: 72.000000
| left: 0.000000
| width: 720.000000
| height: 1136.000000
| visible: 1
| clickable: 0
| checkable: 0
|-> Column childSize:2
| ID: 130
| compid:
| text:
| top: 72.000000
| left: 0.000000
| width: 720.000000
| height: 180.000000
| visible: 1
| clickable: 0
| checkable: 0

......
```

### 获取期望应用路由栈信息

该命令将输出应用页面路由栈的信息，依据栈的创建顺序及其父子关系排列。

> **说明：**
>
> 仅支持通过[Navigation](../arkui-cj/cj-navigation-navigation.md)组件实现页面路由的应用。

命令：

```shell
hidumper -s WindowManagerService -a '-w %windowId% -navigation -c'
```

**使用样例：**

```text
hidumper -s WindowManagerService -a '-w 15 -navigation -c'

-------------------------------[ability]-----------------------------------
----------------------------WindowManagerService---------------------------
WindowName: myapplication0
DisplayId: 0
WinId: 12
Pid: 5908
Type: 1
Mode: 1
Flag: 0
Orientation: 0
IsStartingWindow: false
FirstFrameCallbackCalled: 1
VisibilityState: 0
Focusable: true
DecoStatus: true
IsPrivacyMode: false
isSnapshotSkip: 0
WindowRect: [ 0, 0, 720, 1280 ]
TouchHotAreas: [ 0, 0, 720, 1280 ]
bundleName:com.example.myapplication
moduleName:entry
 LastRequestVsyncTime: 2351504075334
 transactionFlags: [ 5908, 0 ]
 last vsyncId: 527
Navigation number: 4
|-> Navigation ID: 7, Depth: 7, Mode: "SPLIT", NavDestinations:
  | [0]{ ID: 0, Name: "pageOne", Mode: "STANDARD", IsOnShow: "FALSE" }
  | [1]{ ID: 1, Name: "pageTwo", Mode: "STANDARD", IsOnShow: "TRUE" }
|-> Navigation ID: 19, Depth: 7, Mode: "AUTO (STACK)", NavDestinations:
  |-> Navigation ID: 28, Depth: 11, Mode: "STACK", NavDestinations:
  | [0]{ ID: 2, Name: "pageOne", Mode: "STANDARD", IsOnShow: "FALSE" }
  | [1]{ ID: 3, Name: "pageTwo", Mode: "DIALOG", IsOnShow: "FALSE" }
    |-> Navigation ID: 123, Depth: 11, Mode: "AUTO (SPLIT)", NavDestinations:
      | [0]{ ID: 4, Name: "pageFive", Mode: "STANDARD", IsOnShow: "FALSE" }
      | [1]{ ID: 5, Name: "pageSix", Mode: "STANDARD", IsOnShow: "FALSE" }
  | [2]{ ID: 6, Name: "pageThree", Mode: "STANDARD", IsOnShow: "TRUE" }
```

> **说明：**
>
> 同一级别的节点，显示在最下方的节点为栈顶节点。