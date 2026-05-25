# 使用SoundPool播放短音频

使用[SoundPool](./cj-media-kit-intro.md#soundpool)（音频池）提供的接口，可以实现低时延短音播放。

当应用开发时，经常需要使用一些急促简短的音效（如相机快门音效、系统通知音效等），此时建议调用SoundPool，实现一次加载，多次低时延播放。

SoundPool当前支持播放1MB以下的音频资源，大小超过1MB的长音频将截取1MB大小数据进行播放。

本开发指导将以SoundPool进行一次低时延播放音频的过程为例，向开发者讲解如何使用SoundPool。详细的API声明请参见[SoundPool API参考](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#class-soundpool)。

过程包括：创建SoundPool实例，加载音频资源（包括资源的解封装与解码，解码格式请参见[音频解码支持](./cj-avcodec-support-formats.md#音频解码)），设置播放参数（循环模式/播放优先级等），播放控制（播放/停止），释放资源。

在应用开发过程中，开发者应通过监听方法检查当前播放状态并按照一定顺序调用接口，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

> **说明：**
>
> 使用SoundPool播放短音频时，涉及音频焦点管控策略的问题，请参见[音频焦点指南](../audio/cj-audio-playback-concurrency.md)。