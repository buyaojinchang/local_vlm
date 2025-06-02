# Local VLM (Vision Language Model) - 智能图像文字处理工具

这是一个基于 Qwen2.5-VL-3B-Instruct 模型的本地视觉语言模型项目，专注于图像文字识别和多模态处理。

## 项目结构

```
local_vlm/
├── image_test.py          # 基础测试脚本
├── document_process.py    # 文档分析工具
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

### 1. 文档分析工具 (推荐)

专门用于图像文字识别和文档处理的工具。

```bash
# 基本文字识别
python document_process.py --input-path "document.jpg"

# 自定义识别任务
python document_process.py --input-path "photo.png" --task "识别这张图片中的所有文字"

# 保存为文本格式
python document_process.py --input-path "scan.jpg" --output-format txt --task "提取文档内容"
```

#### 参数说明

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `--input-path` | `str` | 必需 | 图像文件路径（jpg、png等） |
| `--output-format` | `"json"` \| `"txt"` | `"json"` | 输出格式 |
| `--task` | `str` | 默认文字提取任务 | 处理任务描述 |

### 2. 基础测试工具

通用的图像和文本处理工具。

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

### 📄 图像文字识别
- **文档扫描**: 识别扫描文档中的文字内容
- **图片文字提取**: 从照片中提取文字信息
- **手写识别**: 对清晰手写文字有一定识别能力

### 🔧 支持的文件格式
- **图像格式**: JPG, PNG, BMP, TIFF, WebP
- **输出格式**: JSON, TXT
- **最大文件大小**: 建议不超过 16MB

### 💬 文本处理
- **对话交互**: 支持纯文本对话
- **内容分析**: 图像内容描述和分析
- **自定义任务**: 灵活的任务定制

## 使用示例

### 文字识别示例

```bash
# 识别发票内容
python document_process.py --input-path "invoice.jpg" --task "提取发票中的关键信息"

# 识别名片文字
python document_process.py --input-path "business_card.png" --task "识别名片上的姓名、电话和邮箱"

# 识别手写笔记
python document_process.py --input-path "notes.jpg" --task "识别手写笔记内容" --output-format txt
```

### 编程方式使用

```python
from document_process import analyze_document

# 文字识别
result = analyze_document(
    input_path="document.jpg",
    output_format="json",
    task="提取图片中的所有文字"
)

# 从图像测试工具导入
from image_test import main

# 图像描述
main(
    content_type="image",
    image_url="photo.jpg",
    text_content="请详细描述这张图片"
)
```

## 输出示例

### JSON 格式输出
```json
{
  "timestamp": "2025-06-02T20:30:45",
  "input_file": "document.jpg",
  "task": "请分析这个文档并提取其中的文字内容",
  "result": "这是一份重要文档，包含以下内容：\n标题：会议纪要\n日期：2025年6月2日\n内容：讨论了项目进展和下一步计划..."
}
```

### TXT 格式输出
```text
处理时间: 2025-06-02T20:30:45
输入文件: document.jpg
处理任务: 请分析这个文档并提取其中的文字内容
结果:
这是一份重要文档，包含以下内容：
标题：会议纪要
日期：2025年6月2日
内容：讨论了项目进展和下一步计划...
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

### 更新依赖
```bash
# 使用 uv
uv pip freeze > requirements.txt

# 或使用 pip
pip freeze > requirements.txt
```

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

