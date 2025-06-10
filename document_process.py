# document_analyzer.py
import tyro
from typing import Literal
import json
from datetime import datetime
from image_test import main as vlm_process

def analyze_document(
    input_path: str,
    output_format: Literal["json", "txt"] = "json",
    description: bool = False,
    extract: bool = False
):
    """简单的文档分析工具 - 支持图像文字识别和文本处理"""
    if description:
        task = "please describe the image in detail"
    if extract:
        task = "please extract all text from the image"
    else:
        NotImplementedError("请至少选择一个任务：描述或提取文本")
    # 调用 VLM 处理
    result = vlm_process(
        content_type="image",
        image_url=input_path,
        text_content=task
    )
    
    # 格式化输出
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "input_file": input_path,
        "task": task,
        "result": result[0] if result else "处理失败"
    }
    
    # 保存结果
    output_file = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{output_format}"
    
    if output_format == "json":
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
    else:  # txt format
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"处理时间: {output_data['timestamp']}\n")
            f.write(f"输入文件: {output_data['input_file']}\n")
            f.write(f"处理任务: {output_data['task']}\n")
            f.write(f"结果:\n{output_data['result']}\n")
    
    print(f"分析完成，结果已保存到: {output_file}")
    return output_file

if __name__ == "__main__":
    tyro.cli(analyze_document)


