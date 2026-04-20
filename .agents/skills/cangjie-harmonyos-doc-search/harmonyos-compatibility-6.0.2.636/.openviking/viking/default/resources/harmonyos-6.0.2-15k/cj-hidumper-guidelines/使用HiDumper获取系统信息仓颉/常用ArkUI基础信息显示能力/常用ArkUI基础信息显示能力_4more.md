## 常用ArkUI基础信息显示能力

ArkUI基于hidumper增强开发了获取组件树等信息的能力。

### 获取应用窗口信息

打印全量窗口信息，可以在全量信息中找出对应窗口的WinId，将该WinId作为参数传递给其他命令以获取相关信息。

```shell
hdc shell hidumper -s WindowManagerService -a '-a'
```

 **使用样例：**

```text
-------------------------------[ability]-----------------------------------

----------------------------WindowManagerService---------------------------
------------------------------ScreenGroup 1--------------------------------
WindowName             DisplayId Pid     WinId Type Mode Flag ZOrd Orientation [ x    y    w    h    ]
ScreenLockWindow       0         1274    2     2110 1    0    4    0           [ 0    0    720  1280 ]
SystemUi_NavigationBar 0         1274    5     2112 102  1    3    0           [ 0    1208 720  72   ]
SystemUi_StatusBar     0         1274    4     2108 102  1    2    0           [ 0    0    720  72   ]
settings0              0         10733   11    1    1    1    1    0           [ 0    72   720  1136 ]
EntryView              0         1546    8     2001 1    0    0    8           [ 0    0    720  1280 ]
---------------------------------------------------------------------------
SystemUi_VolumePanel   0         1274    3     2111 1    1    -1   0           [ 0    0    0    0    ]
SystemUi_DropdownPan   0         1274    6     2109 1    1    -1   0           [ 0    0    0    0    ]
SystemUi_BannerNotic   0         1274    7     2111 1    1    -1   0           [ 0    0    0    0    ]
RecentView             0         1546    9     2115 1    1    -1   0           [ 0    0    0    0    ]
imeWindow              0         1530    10    2105 1    1    -1   0           [ 0    0    0    0    ]
Focus window: 2
total window num: 10
```

常见windowName与内置应用窗口的对应关系：
|windowName|内置应用窗口|
|---|---|
| EntryView|桌面|
| RecentView|最近任务|
| SystemUi_NavigationBar|三键导航|
|  SystemUi_StatusBar|状态栏|
| ScreenLockWindow|锁屏|

### 获取期望应用组件树

如果需要查看应用中所有组件的信息，可以通过下列命令实现。

```shell
hdc shell "hidumper -s WindowManagerService -a '-w %windowId% -element'"
```

windowId是期望应用的窗口ID。

**使用样例：**

```text
hdc shell "hidumper -s WindowManagerService -a '-w 5 -element'"

-------------------------------[ability]-----------------------------------
----------------------------WindowManagerService---------------------------
WindowName: SystemUi_NavigationBar
DisplayId: 0
WinId: 5
Pid: 1274
Type: 2112
Mode: 102
Flag: 1
Orientation: 0
IsStartingWindow: false
FirstFrameCallbackCalled: 0
IsVisible: false
WindowRect: [ 0, 1208, 720, 72 ]
TouchHotAreas: [ 0, 1208, 720, 72 ]
  |-> RootElement childSize:1
    | ID: 0
    | elmtId: -1
    | retakeID: 16
    | Active: Y
    |-> StackElement childSize:2
      | ID: 1
      | elmtId: -1
      | retakeID: 14
      | Active: Y
      |-> StageElement childSize:1
        | ID: 2
        | elmtId: -1
        | retakeID: 13
        | Active: Y
        |-> PageElement childSize:1
          | ID: 3
          | elmtId: -1
          | retakeID: 569
          | Active: Y
......
```

### 获取应用中指定Node的组件信息

如果只需要查看组件中某一节点的组件信息，可以通过下列命令实现。

```shell
hdc shell "hidumper -s WindowManagerService -a '-w %windowId% -element -lastpage %nodeID%'"
```

windowId是应用的窗口ID，nodeID是指定Node的ID。可以通过获取期望应用组件树的操作获取nodeID。

**使用样例：**

```text
hdc shell "hidumper -s WindowManagerService -a '-w 5 -element -lastpage 3'"

-------------------------------[ability]-----------------------------------
----------------------------WindowManagerService---------------------------
WindowName: SystemUi_NavigationBar
DisplayId: 0
WinId: 5
Pid: 1274
Type: 2112
Mode: 102
Flag: 1
Orientation: 0
IsStartingWindow: false
FirstFrameCallbackCalled: 0
IsVisible: false
WindowRect: [ 0, 1208, 720, 72 ]
TouchHotAreas: [ 0, 1208, 720, 72 ]
    |-> PageElement childSize:1
        | ID: 3
        | elmtId: -1
        | retakeID: 569
        | Active: Y
......
```