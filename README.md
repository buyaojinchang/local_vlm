# Local VLM (Vision Language Model)

这是一个基于 Qwen2.5-VL-3B-Instruct 模型的本地视觉语言模型项目，支持图像和文本的多模态处理。

## 项目结构

```
local_vlm/
├── image_test.py          # 主要测试脚本
├── requirements.txt       # 项目依赖文件
├── README.md             # 项目说明文档
└── models/
    └── Qwen2.5-VL-3B-Instruct/  # 本地模型文件
        ├── config.json
        ├── model-*.safetensors
        ├── tokenizer.json
        └── ...
```

## 快速开始

### 环境设置

#### 方法1：使用 uv（推荐）

```bash
# 克隆或下载项目到本地
cd local_vlm

# 创建虚拟环境
uv venv

# 激活环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows

# 安装依赖
uv pip install -r requirements.txt
```

#### 方法2：使用 pip

```bash
# 创建虚拟环境
python -m venv .venv

# 激活环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 下载模型

确保模型文件位于 `models/Qwen2.5-VL-3B-Instruct/` 目录下。如果没有本地模型，可以：

1. 从 [Hugging Face](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) 下载
2. 或修改代码中的模型路径为在线地址

## 使用方法

### 基本使用

```bash
# 使用默认参数运行（图像描述）
python image_test.py

# 查看所有可用参数
python image_test.py --help
```

### 命令行参数

使用 `tyro` 库提供的命令行界面：

```bash
# 处理图像内容（默认）
python image_test.py --content-type image --image-url "https://example.com/image.jpg" --text-content "描述这张图片"

# 处理本地图像文件
python image_test.py --content-type image --image-url "path/to/your/image.jpg" --text-content "这张图片里有什么？"

# 纯文本对话
python image_test.py --content-type text --text-content "你好，请介绍一下你自己"
```

### 参数说明

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `--content-type` | `"image"` \| `"text"` | `"image"` | 输入内容类型 |
| `--image-url` | `str` | Qwen 官方示例图片 | 图像URL或本地路径 |
| `--text-content` | `str` | `"Describe this image."` | 文本提示内容 |

### 编程方式使用

```python
from image_test import main

# 图像描述
main(
    content_type="image",
    image_url="https://example.com/image.jpg",
    text_content="请详细描述这张图片"
)

# 纯文本对话
main(
    content_type="text", 
    text_content="你好，请介绍一下你自己"
)
```

## 依赖管理

### 更新依赖

如果添加了新的依赖包，记得更新 requirements.txt：

```bash
# 使用 uv
uv pip freeze > requirements.txt

# 或使用 pip
pip freeze > requirements.txt
```

### 主要依赖说明

- **transformers**: Hugging Face 模型库
- **torch/torchvision**: PyTorch 深度学习框架
- **qwen-vl-utils**: Qwen 视觉处理工具包
- **tyro**: 命令行参数解析
- **accelerate**: 模型加速库

## 模型信息

本项目使用的是 **Qwen2.5-VL-3B-Instruct** 模型，这是一个强大的视觉语言模型，具有以下特点：

- **多模态理解**：支持图像、视频和文本的联合处理
- **高精度识别**：能够识别图像中的物体、文字、图表等
- **长文本处理**：支持最长 32,768 tokens 的上下文
- **结构化输出**：支持生成 JSON 等结构化格式的输出

更多模型信息请参考：[models/Qwen2.5-VL-3B-Instruct/README.md](models/Qwen2.5-VL-3B-Instruct/README.md)

## 功能特性

### 支持的输入格式

1. **图像处理**
   - 网络图片 URL
   - 本地图片文件路径  
   - Base64 编码图片

2. **视频处理**（如需要）
   - 本地视频文件
   - 网络视频 URL
   - 视频帧序列

3. **文本处理**
   - 纯文本对话
   - 多轮对话

### 主要能力

- 🖼️ **图像理解**：描述图像内容、识别物体、分析场景
- 📊 **文档分析**：处理图表、表格、文档扫描件
- 🎯 **视觉定位**：生成边界框和坐标点
- 📝 **结构化输出**：支持 JSON 格式的结构化数据提取
- 💬 **对话交互**：支持基于视觉内容的多轮对话

## 系统要求

### 硬件要求

- **GPU**: 推荐使用 CUDA 兼容的 GPU（至少 8GB 显存）
- **内存**: 推荐至少 16GB RAM
- **存储**: 模型文件约占用 6-8GB 空间

### 软件要求

- Python 3.8+
- CUDA 11.8+ (如使用 GPU)
- Linux/macOS/Windows

## 故障排除

### 常见问题

1. **导入错误**：确保已正确安装所有依赖
   ```bash
   pip install -r requirements.txt
   ```

2. **CUDA 内存不足**：减少批处理大小或使用 CPU
   ```python
   # 在代码中修改 device_map
   device_map="cpu"  # 或 "auto"
   ```

3. **模型文件缺失**：检查模型路径或下载完整模型

## 许可证

本项目使用的 Qwen2.5-VL 模型遵循 Qwen Research License Agreement。详情请参考 [models/Qwen2.5-VL-3B-Instruct/LICENSE](models/Qwen2.5-VL-3B-Instruct/LICENSE)。

## 参考资料

- [Qwen2.5-VL 官方博客](https://qwenlm.github.io/blog/qwen2.5-vl/)
- [Qwen2.5-VL GitHub 仓库](https://github.com/QwenLM/Qwen2.5-VL)
- [Hugging Face 模型页面](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)
- [tyro 文档](https://brentyi.github.io/tyro/)

