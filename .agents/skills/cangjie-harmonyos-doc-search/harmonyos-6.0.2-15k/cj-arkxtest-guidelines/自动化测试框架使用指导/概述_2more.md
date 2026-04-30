## 概述

仓颉自动化测试框架由两个概念组成，分别是仓颉HarmonyOS单元测试框架与UiTest。

仓颉HarmonyOS单元测试框架基于仓颉语言自带的单元测试库std.unittest实现，其提供了基础的单元测试用例编写、单元测试用例执行与测试报告生成能力。在std.unittest的基础上，使用TestRunner对OH平台进行了适配，使得其能在应用中使用。

UiTest提供了UI组件的查找和操作能力，用户通过调用UiTest提供的接口可以编写测试脚本以实现UI自动化测试。UiTest框架同时也以hdc shell命令的形式对外提供了获取截屏、获取控件树、录制用户操作、注入UI模拟操作等辅助测试能力。

本指南介绍了仓颉自动化测试框架的主要功能、实现原理、环境准备，以及测试脚本编写和执行方法。

## 实现原理

测试框架分为单元测试框架和UI测试框架。

单元测试框架是测试框架的基础底座，提供了最基本的用例识别、调度、执行及结果汇总的能力。

UI测试框架主要对外提供了UiTest API供开发人员在对应测试场景调用，而其脚本的运行基础仍是单元测试框架。

### 单元测试框架

- 单元测试框架主要功能

  ![UnitTest.jpg](figures/UnitTest.jpg)

- 脚本基础流程

    - 根据-s unittest参数找到对应的TestRunner.registerCreator，实例化TestRunner，并依次执行onPrepare和onRun
    - onRun中进行启动参数的解析，识别出执行哪些测试用例，以及timeout等信息
    - 调用仓颉内核unittest初始化测试套并执行测试套，测试结果以xml形式保存于设备`/data/app/el1/100/base/${bundleName}/tests`
    - 所有指定的测试套执行结束后，读取xml测试报告，打印到终端，以及hilog日志

### UI测试框架

- UI测试框架主要功能

![Uitest.png](figures/Uitest.png)