from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch
import tyro
from typing import Literal

def main(
    content_type: Literal["image", "text"] = "image",
    image_url: str = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
    text_content: str = "Describe this image."
):
    # ...existing code...
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        "models/Qwen2.5-VL-3B-Instruct",
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

    processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct")

    # 根据输入的 content_type 构建 messages
    if content_type == "image":
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": image_url,
                    },
                    {"type": "text", "text": text_content},
                ],
            }
        ]
    else:  # content_type == "text"
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": text_content},
                ],
            }
        ]

    # ...existing inference code...
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")

    generated_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    print(output_text)
    return output_text
if __name__ == "__main__":
    result = tyro.cli(main)