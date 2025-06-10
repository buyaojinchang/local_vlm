# Local VLM (Vision Language Model) - 智能图像文字处理工具

这是一个基于 Qwen2.5-VL-3B-Instruct 模型的本地视觉语言模型项目，专注于图像文字识别和多模态处理。

## 项目结构

```
local_vlm/
├── image_test.py          # 基础测试脚本
├── document_process.py    # 文档与图像分析工具
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

```bash
# 创建模型目录
mkdir -p models

# 使用 huggingface-hub 下载（推荐）
pip install huggingface-hub
huggingface-cli download Qwen/Qwen2.5-VL-3B-Instruct --local-dir models/Qwen2.5-VL-3B-Instruct

# 或者使用 git lfs
git lfs install
git clone https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct models/Qwen2.5-VL-3B-Instruct
```

## 使用方法

### 1. 文档与图像分析工具 (`document_process.py`)

此工具集成了图像理解（描述）和文字提取功能。

```bash
# 提取图像中的文字
python document_process.py --input-path "document.jpg" --extract

# 详细描述图像内容
python document_process.py --input-path "photo.png" --description

# 同时指定描述和提取（当前版本将优先执行文字提取任务）
python document_process.py --input-path "scan.jpg" --description --extract --output-format txt
```

#### 参数说明

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `--input-path` | `str` | 必需 | 图像文件路径（jpg、png等） |
| `--output-format` | `"json"` \| `"txt"` | `"json"` | 输出结果的格式 |
| `--description` | `bool` | `False` | 对图像内容进行详细描述 |
| `--extract` | `bool` | `False` | 从图像中提取所有文本信息 |

**注意**: 必须至少指定 `--description` 或 `--extract` 中的一个参数。如果同时指定了 `--description` 和 `--extract`，当前脚本会优先执行文本提取任务。

### 2. 基础测试工具 (`image_test.py`)

通用的图像和文本处理工具，用于更灵活的自定义任务。

```bash
# 图像描述
python image_test.py --content-type image --image-url "photo.jpg" --text-content "描述这张图片"

# 纯文本对话
python image_test.py --content-type text --text-content "你好，请介绍一下你自己"
```

#### 参数说明

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `--content-type` | `"image"` \| `"text"` | `"image"` | 输入内容类型 |
| `--image-url` | `str` | Qwen 官方示例图片 | 图像URL或本地路径 |
| `--text-content` | `str` | `"Describe this image."` | 文本提示内容 |

## 主要功能

### 📄 图像分析与处理 (`document_process.py`)
- **文字提取**: 从各类图像（文档扫描件、照片、截图等）中识别并提取文本。
- **图像理解**: 对图像内容进行详细的场景描述和物体识别。
- **格式化输出**: 支持将分析结果保存为 JSON 或 TXT 文件。

### 🔧 通用多模态处理 (`image_test.py`)
- **灵活的图像处理**: 支持通过 URL 或本地路径加载图像，并配合自定义文本提示进行处理。
- **纯文本交互**: 支持与模型进行纯文本的问答和对话。

### ✨ 共同特性
- **基于 Qwen2.5-VL**: 利用强大的视觉语言模型进行处理。
- **本地化运行**: 模型和代码均在本地运行，保障数据隐私。
- **易于使用**: 提供清晰的命令行参数。

## 使用示例

### 使用 `document_process.py`

```bash
# 提取发票图片中的文字，并保存为json
python document_process.py --input-path "invoice.png" --extract --output-format json

# 描述一张风景照片的内容，并保存为txt
python document_process.py --input-path "landscape.jpg" --description --output-format txt

# 如果一张图片既想提取文字也想描述（注意：当前优先提取文字）
python document_process.py --input-path "poster.jpg" --extract --description
```

### 使用 `image_test.py`

```bash
# 让模型识别图片中的主要物体
python image_test.py --image-url "my_pet.jpg" --text-content "图片中的主要物体是什么？"

# 进行一个简单的数学问答（纯文本）
python image_test.py --content-type text --text-content "一加一等于几？"
```

## 系统要求

### 硬件要求
- **GPU**: 推荐使用 CUDA 兼容的 GPU（至少 8GB 显存）
- **内存**: 推荐至少 16GB RAM
- **存储**: 模型文件约占用 6-8GB 空间

### 软件要求
- Python 3.8+
- CUDA 11.8+ (如使用 GPU)
- Linux/macOS/Windows

## 优化建议

### 提高识别准确率
1. **图像质量**: 使用高分辨率、清晰的图像
2. **光线条件**: 确保图像光线充足，对比度良好
3. **文字大小**: 文字应该足够大，建议至少 12pt

### 性能优化
1. **GPU 加速**: 使用 CUDA GPU 可显著提升处理速度
2. **图像尺寸**: 适当调整图像尺寸可以平衡速度和准确率
3. **批量处理**: 对于大量文档，可以编写批处理脚本

## 依赖管理

### 主要依赖
- **transformers**: Hugging Face 模型库
- **torch/torchvision**: PyTorch 深度学习框架  
- **qwen-vl-utils**: Qwen 视觉处理工具包
- **tyro**: 命令行参数解析

## 故障排除

### 常见问题

1. **导入错误**: 确保已正确安装所有依赖
   ```bash
   pip install -r requirements.txt
   ```

2. **CUDA 内存不足**: 使用 CPU 模式
   ```python
   device_map="cpu"
   ```

3. **识别效果差**: 检查图像质量和文字清晰度

4. **文件格式不支持**: 确保使用 JPG、PNG 等支持的格式

## 许可证

本项目使用的 Qwen2.5-VL 模型遵循 Qwen Research License Agreement。

## 参考资料

- [Qwen2.5-VL 官方博客](https://qwenlm.github.io/blog/qwen2.5-vl/)
- [Hugging Face 模型页面](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)
- [tyro 文档](https://brentyi.github.io/tyro/)

## 贡献与支持

欢迎提交 Issue 和 Pull Request 来改进这个项目！如果这个工具对您有帮助，请给项目点个星标 ⭐

