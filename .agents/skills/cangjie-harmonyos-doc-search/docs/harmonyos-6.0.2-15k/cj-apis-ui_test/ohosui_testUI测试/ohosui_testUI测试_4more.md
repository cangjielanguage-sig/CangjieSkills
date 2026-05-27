# ohos.ui_test（UI测试）

ui_test提供模拟UI操作的能力，供开发者在测试场景使用，主要支持如点击、双击、长按、滑动等UI操作能力。

该模块提供以下功能：

- [UITest](#class-uitest): [UITest](#class-uitest)类只包含一个静态方法setup，用于初始化ui_test库。
- [On](#class-on)：提供控件特征描述能力，用于控件筛选匹配查找。
- [UIComponent](#class-uicomponent)：代表UI界面上的指定控件，提供控件属性获取、控件点击、滑动查找、文本注入等能力。
- [Driver](#class-driver)：入口类，提供控件匹配、查找、按键注入、坐标点击或滑动、截图等能力。
- [UiWindow](#class-uiwindow)：入口类，提供窗口属性获取、窗口拖动、调整窗口大小等能力。

## 导入模块

```cangjie
import kit.TestKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## 运行测试

### 准备工作

- 将支持uitest测试框架的设备连接上pc，pc上装好对应驱动和hdc服务。
- 对于刷机后第一次使用uitest框架的设备，执行`hdc shell param set persist.ace.testmode.enabled 1`并重启设备进行ace使能，保证设备可以通过无障碍服务获取到arkui控件节点信息。
- 执行`hdc shell param set persist.sys.suspend_manager_enabled 0`并重启设备，关闭后台应用冻结机制。

### 测试命令

```text
hdc shell aa test -b com.example.myapplication -m entry -s unittest CJTestRunner
```

- 这里的`-b com.example.myapplication -m entry`按照app里实际的bundle name和module name填。
- 最后的`CJTestRunner`是TestRunner.registerCreator注册TestRunner的第一个参数。