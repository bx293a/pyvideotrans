# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setini.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore,  QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMessageBox

from videotrans.configure import config

class Ui_setini(object):
    def setupUi(self, setini):
        setini.setObjectName("setini")
        setini.setWindowModality(QtCore.Qt.NonModal)
        setini.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setini.sizePolicy().hasHeightForWidth())
        setini.setSizePolicy(sizePolicy)
        setini.setMaximumSize(QtCore.QSize(800, 600))

        self.verticalLayoutWidget = QtWidgets.QWidget(setini)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 760, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")

        scroll_area = QtWidgets.QScrollArea(setini)
        scroll_area.setWidgetResizable(True)
        scroll_area.setAlignment(Qt.AlignmentFlag.AlignTop)

        box = QtWidgets.QWidget()  # 创建新的 QWidget，它将承载你的 QHBoxLayouts
        box.setLayout(QtWidgets.QVBoxLayout())

        self.notices={
            "ai302_models": "填写302.ai用于翻译的模型名字，以英文逗号分隔",
            "ai302tts_models": "填写302.ai用于配音的模型名字，以英文逗号分隔",
            "lang": "设置软件界面语言，修改后需要重启软件",
            "crf": "视频转码时损失控制，0=无损，51=损失最大，默认13",
            "cuda_qp": "在 NVIDIA cuda上是否使用 qp代替crf，true=是，false=否",
            "preset": "用于控制输出视频质量和大小，越快质量越差",
            "ffmpeg_cmd": "自定义ffmpeg命令参数， 将添加在倒数第二个位置上,例如  -bf 7 -b_ref_mode middle",
            "video_codec": "采用 libx264 编码或 libx265编码，264兼容性更好，265压缩比更大清晰度更高",
            "chatgpt_model": "可供选择的chatGPT模型，以英文逗号分隔",
            "azure_model": "可供选择的模型，以英文逗号分隔",
            "localllm_model": "可供选择的模型，以英文逗号分隔",
            "zijiehuoshan_model": "填写在字节火山方舟创建的推理接入点名称 创建方法见 https://pyvideotrans.com/zijiehuoshan",
            "model_list": "faster模式和openai模式下的模型名字",
            "audio_rate": "音频最大加速倍数，默认3，即最大加速到 3倍速度，需设置1-100的数字，比如3，代表最大加速3倍",
            "video_rate": "视频慢速倍数：大于1的数，代表最大允许慢速多少倍，0或1代表不进行视频慢放",
            "remove_silence": "是否移除配音末尾空白，true=移除，false=不移除",
            "remove_srt_silence": "是否移除原始字幕时长大于配音时长 的静音，比如原时长5s，配音后3s，是否移除这2s静音，true=移除，false=不移除",
            "remove_white_ms": "移除2条字幕间的静音长度ms，比如100ms，即如果两条字幕间的间隔大于100ms时，将移除100ms, -1=完全移除",
            "force_edit_srt": "true=强制修改字幕时间轴以便匹配声音，false=不修改，保持原始字幕时间轴，不修改可能导致字幕和声音不匹配",
            "vad": "faster-whisper字幕整体识别模式时启用VAD",
            "overall_silence": "最小静音片段ms，默认250ms ",
            "overall_maxsecs": "语句祖达持续秒数",
            "overall_threshold": "VAD阈值",
            "overall_speech_pad_ms": "VAD pad值",
            "voice_silence": "均等分割模式下静音片段",
            "interval_split": "均等分割模式下每个片段时长秒数",
            "trans_thread": "同时翻译的字幕条数",
            "retries": "翻译出错时重试次数",
            "dubbing_thread": "同时配音的字幕条数",
            "countdown_sec": "暂停时倒计时秒数",
            "backaudio_volume": "背景音频音量值为原本的倍数",
            "loop_backaudio": "如果背景音频时长短于视频，是否重复播放背景音，默认否",
            "cuda_com_type": "faster模式时cuda数据类型，int8=消耗资源少，速度快，精度低，float32=消耗资源多，速度慢，精度高，int8_float16=设备自选",
            "initial_prompt_zh": "发送给whisper模型的提示词",
            "whisper_threads": "faster模式下，字幕识别时，cpu进程",
            "whisper_worker": "faster模式下，字幕识别时，同时工作进程",
            "beam_size": "字幕识别时精度调整，1-5，1=消耗显存最低，5=消耗显存最多",
            "best_of": "字幕识别时精度调整，1-5，1=消耗显存最低，5=消耗显存最多",
            "temperature": "0=占用更少GPU资源但效果略差，1=占用更多GPU资源同时效果更好",
            "condition_on_previous_text": "true=占用更多GPU效果更好，false=占用更少GPU效果略差",
            "fontsize": "硬字幕字体像素",
            "fontname": "硬字幕时字体名字",
            "fontcolor": "设置字体的颜色，注意&H后的6个字符，每2个字母分别代表 BGR 颜色，即2位蓝色/2位绿色/2位红色，同同时常见的RGB色色颠倒的。",
            "fontbordercolor": "设置字体边框颜色，注意&H后的6个字符，每2个字母分别代表 BGR 颜色，即2位蓝色/2位绿色/2位红色，同同时常见的RGB色色颠倒的。",
            "subtitle_bottom": "字幕默认位于视频底部，此处可设置大于0的数值，代表字幕上移多少距离，注意最大不可大于(视频高度-20),也就是要保留至少20的高度用于显示字幕，否则字幕将不可见",
            "cjk_len": "中日韩硬字幕时一行长度字符个数，多于这个将换行",
            "other_len": "其他语言硬字幕时换行长度，多于这个字符数量将换行",
            "zh_hant_s": "强制将繁体字幕转为简体",
            "azure_lines": "azureTTS 批量行数",
            "chattts_voice": "chatTTS音色值"
        }
        if config.defaulelang != 'zh':
            self.notices = {
                "ai302_models": "Enter the names of the models used by 302.ai for translation, separated by English commas",
                "ai302tts_models": "Enter the names of the models used by 302.ai for dubbing, separated by English commas",
                "lang": "Set the language of the software interface. Restart the software after modification",
                "crf": "Loss control when video transcoding, 0=no loss, 51=maximum loss, default is 13",
                "cuda_qp": "Whether to use qp instead of crf on NVIDIA cuda, true=yes, false=no",
                "preset": "Used to control the quality and size of the output video, the faster the worse the quality",
                "ffmpeg_cmd": "Custom FFmpeg command parameters, added to the second-to-last position, for example -bf 7 -b_ref_mode middle",
                "video_codec": "Use libx264 encoding or libx265 encoding, 264 has better compatibility, 265 has higher compression ratio and clearer image",
                "chatgpt_model": "Selectable chatGPT models, separated by English commas",
                "azure_model": "Selectable models, separated by English commas",
                "localllm_model": "Selectable models, separated by English commas",
                "zijiehuoshan_model": "Enter the name of the inference access point created on Byte Volcano Ark. See the creation method at https://pyvideotrans.com/zijiehuoshan",
                "model_list": "Model names in faster mode and openai mode",
                "audio_rate": "Maximum audio acceleration rate, default is 3, i.e., up to 3 times the speed. Set a number between 1-100, such as 3, representing a maximum acceleration of 3 times",
                "video_rate": "Video slow-motion multiple: a number greater than 1, representing the maximum allowable slow-motion multiple, 0 or 1 represents no video slow motion",
                "remove_silence": "Whether to remove the blank at the end of the dubbing, true=remove, false=do not remove",
                "remove_srt_silence": "Whether to remove the silence when the original subtitle duration is longer than the dubbing duration, for example, the original duration is 5s, and after dubbing it is 3s, whether to remove these 2s of silence, true=remove, false=do not remove",
                "remove_white_ms": "Remove the silence length between two subtitles in milliseconds, for example, 100ms, that is, if the interval between two subtitles is greater than 100ms, 100ms will be removed, -1=remove completely",
                "force_edit_srt": "true=Force to modify the subtitle timeline to match the sound, false=Do not modify, keep the original subtitle timeline, not modifying may cause the subtitle and sound to be mismatched",
                "vad": "Enable VAD when using the faster-whisper subtitle overall recognition mode",
                "overall_silence": "Minimum silence fragment ms, default is 250ms",
                "overall_maxsecs": "Statement duration in seconds",
                "overall_threshold": "VAD threshold",
                "overall_speech_pad_ms": "VAD pad value",
                "voice_silence": "Silence fragments in equal division mode",
                "interval_split": "Duration of each segment in seconds in equal division mode",
                "trans_thread": "Number of subtitle bars translated simultaneously",
                "retries": "Number of retries when translation fails",
                "dubbing_thread": "Number of subtitle bars dubbed simultaneously",
                "countdown_sec": "Countdown seconds when paused",
                "backaudio_volume": "Background audio volume is a multiple of the original",
                "loop_backaudio": "If the background audio duration is shorter than the video, whether to play the background sound repeatedly, default is no",
                "cuda_com_type": "Cuda data type when in faster mode, int8=less resource consumption, fast, low precision, float32=more resource consumption, slow, high precision, int8_float16=device selected",
                "initial_prompt_zh": "Prompt words sent to the whisper model",
                "whisper_threads": "Subtitle recognition in faster mode, CPU process",
                "whisper_worker": "Subtitle recognition in faster mode, simultaneous working processes",
                "beam_size": "Precision adjustment during subtitle recognition, 1-5, 1=lowest consumption of video memory, 5=most consumption of video memory",
                "best_of": "Precision adjustment during subtitle recognition, 1-5, 1=lowest consumption of video memory, 5=most consumption of video memory",
                "temperature": "0=less GPU resource consumption but slightly worse effect, 1=more GPU resource consumption and better effect",
                "condition_on_previous_text": "true=more GPU resource consumption and better effect, false=less GPU resource consumption and slightly worse effect",
                "fontsize": "Hard subtitle font pixel size",
                "fontname": "Font name when using hard subtitles",
                "fontcolor": "Set the font color, note the 6 characters after &H, each 2 letters represent BGR color, i.e., 2 bits for blue/2 bits for green/2 bits for red, which is the opposite of the commonly seen RGB color.",
                "fontbordercolor": "Set the font border color, note the 6 characters after &H, each 2 letters represent BGR color, i.e., 2 bits for blue/2 bits for green/2 bits for red, which is the opposite of the commonly seen RGB color.",
                "subtitle_bottom": "Subtitles are located at the bottom of the video by default, here you can set a value greater than 0, representing how much the subtitles are moved up, note that the maximum should not be greater than (video height - 20), that is, at least 20 height should be reserved for displaying subtitles, otherwise the subtitles will not be visible",
                "cjk_len": "The number of characters in a line of CJK hard subtitles, more than this will be wrapped",
                "other_len": "The line break length for other languages when using hard subtitles, more than this number of characters will be wrapped",
                "zh_hant_s": "Force traditional Chinese subtitles to be converted to simplified Chinese",
                "azure_lines": "AzureTTS batch line count",
                "chattts_voice": "chatTTS voice value"
            }



        # 界面语言
        for key,val in config.settings.items():
            tmp = QtWidgets.QHBoxLayout()
            tmp_0=QtWidgets.QPushButton()
            tmp_0.setStyleSheet("""background-color:transparent;text-align:right""")
            tmp_0.setFixedWidth(150)
            tmp_0.setText(key)
            tmp_0.setObjectName(f'btn_{key}')
            tmp_0.setToolTip('?help')
            tmp_0.setCursor(Qt.PointingHandCursor)
            hlp=self.notices[key] if key in self.notices else ""

            tmp_1 = QtWidgets.QLineEdit()
            tmp_1.setMinimumSize(QtCore.QSize(0, 30))
            tmp_1.setText(str(val))
            tmp_1.setToolTip(hlp)
            tmp_1.setObjectName(key)
            tmp.addWidget(tmp_0)
            tmp.addWidget(tmp_1)
            box.layout().addLayout(tmp)

        # 第2个


        box.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(box)
        self.layout.addWidget(scroll_area)



        self.set_ok = QtWidgets.QPushButton(setini)
        self.set_ok.setGeometry(QtCore.QRect(325, 550, 150, 35))
        self.set_ok.setMinimumSize(QtCore.QSize(0, 35))
        self.set_ok.setObjectName("set_ok")

        self.retranslateUi(setini)
        QtCore.QMetaObject.connectSlotsByName(setini)

    def retranslateUi(self, setini):
        setini.setWindowTitle('高级设置/原set.ini' if config.defaulelang=='zh' else 'Advanced Settings/set.ini')
        self.set_ok.setText('保存并关闭' if config.defaulelang=='zh' else "Save and Close")
