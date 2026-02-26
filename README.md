# Cangjie Skills
## 一、cangjie-dev-harmonyos
本 Skill 赋能 Claude 使用仓颉进行 HarmonyOS 应用开发。

### 首次使用
在首次启动开发查询仓颉知识库时，系统会自动构建本地文档树（hm-docs）和向量数据库（chroma-db），预计耗时约 1 分钟。资源加载策略如下：

1. 检测到已解压目录：直接读取并使用

2. 仅检测到本地压缩包：自动执行解压操作

3. 未检测到本地资源：自动触发下载并完成构建


💡 快速跳过构建（可选）

为了节省初始化的等待时间，您可以手动下载以下压缩包，并直接解压至项目的 scripts/ 目录下，即可跳过上述自动构建步骤：

hm-docs压缩包目录：https://my.feishu.cn/file/I3BEbJOyBokdtAxbr18cPUlHnDb

chroma-db压缩包目录：https://my.feishu.cn/file/RqY3bprAKoIm9Lxsfa4czYEwnJd

图示是根据skill赋能的CLAUDE自动化应用开发成果示例。  
![微信图片_20260225115922_232_63.png](https://raw.gitcode.com/user-images/assets/9193544/ad4b63c4-f26d-4fe4-a33e-dfded2054010/微信图片_20260225115922_232_63.png '微信图片_20260225115922_232_63.png')
